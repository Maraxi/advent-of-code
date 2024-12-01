const std = @import("std");

const conf = struct {
    func: u1 = 0,
    input: []const u8 = "",
};

fn get_args(allocator: std.mem.Allocator) conf {
    var args = try std.process.argsWithAllocator(allocator);
    defer args.deinit();

    _ = args.skip();

    var config: conf = .{};
    if (std.mem.eql(u8, args.next() orelse "", "1")) {
        config.func = 1;
    }
    config.input = args.next() orelse "01.input";

    return config;
}

fn readFile(allocator: std.mem.Allocator, filename: []const u8) ![]u8 {
    const file = try std.fs.cwd().openFile(filename, .{});

    const stat = try file.stat();
    const buff = try file.readToEndAlloc(allocator, stat.size);
    return buff;
}

pub fn main() void {
    const allocator = std.heap.page_allocator;

    const args = get_args(allocator);

    const buff = readFile(allocator, args.input) catch {
        std.debug.print("Can not open file", .{});
        return;
    };
    defer allocator.free(buff);

    var lines = std.mem.split(u8, buff, "\n");

    var list = std.ArrayList([]const u8).init(allocator);
    defer list.deinit();

    while (lines.next()) |line| {
        if (std.mem.eql(u8, line, "")) break;
        list.append(line) catch unreachable;
        // std.debug.print("{s}\n", .{line});
    }

    // std.debug.print("{s}", .{list.items});

    if (args.func == 0) {
        task0(allocator, list) catch {};
    } else {
        task1(allocator, list) catch {};
    }
}

fn task0(allocator: std.mem.Allocator, list: std.ArrayList([]const u8)) !void {
    std.debug.print("{}\n", .{list.items.len});

    var left = std.ArrayList(i64).init(allocator);
    defer left.deinit();
    var right = std.ArrayList(i64).init(allocator);
    defer right.deinit();

    for (list.items) |line| {
        var it = std.mem.splitSequence(u8, line, "   ");
        try left.append(try std.fmt.parseUnsigned(i64, it.next().?, 10));
        try right.append(try std.fmt.parseUnsigned(i64, it.next().?, 10));
    }

    std.mem.sort(i64, left.items, {}, std.sort.asc(i64));
    std.mem.sort(i64, right.items, {}, std.sort.asc(i64));

    // std.debug.print("{any} {any}\n", .{ left.items, right.items });

    var total: u64 = 0;
    for (left.items, right.items) |l, r| {
        // std.debug.print("{} {}\n", .{ l, r });
        total += @abs(r - l);
    }

    std.debug.print("{}", .{total});
}

fn task1(allocator: std.mem.Allocator, list: anytype) !void {
    std.debug.print("{}\n", .{list.items.len});

    var left = std.ArrayList(u64).init(allocator);
    defer left.deinit();
    var right = std.AutoHashMap(u64, u64).init(allocator);
    defer right.deinit();

    for (list.items) |line| {
        var it = std.mem.splitSequence(u8, line, "   ");
        try left.append(try std.fmt.parseUnsigned(u64, it.next().?, 10));
        const r = try std.fmt.parseUnsigned(u64, it.next().?, 10);
        const entry = try right.getOrPut(r);
        if (entry.found_existing) {
            entry.value_ptr.* += 1;
        } else {
            entry.value_ptr.* = 1;
        }
    }

    var total: u64 = 0;
    for (left.items) |l| {
        const entry = right.get(l) orelse 0;
        // std.debug.print("{} {}\n", .{ l, entry });
        total += l * entry;
    }

    std.debug.print("{}", .{total});
}
