const std = @import("std");
const print = std.debug.print;
const parseInt = std.fmt.parseInt;
const allocator = std.heap.page_allocator;

const conf = struct {
    func: u1 = 0,
    input: []const u8 = "",
};

fn get_args() conf {
    var args = try std.process.argsWithAllocator(allocator);
    defer args.deinit();

    _ = args.skip();

    var config: conf = .{};
    if (std.mem.eql(u8, args.next() orelse "", "1")) {
        config.func = 1;
    }
    config.input = args.next() orelse "02.input";

    return config;
}

fn readFile(filename: []const u8) ![]u8 {
    const file = try std.fs.cwd().openFile(filename, .{});

    const stat = try file.stat();
    const buff = try file.readToEndAlloc(allocator, stat.size);
    return buff;
}

pub fn main() void {
    const args = get_args();

    const buff = readFile(args.input) catch {
        print("Can not open file", .{});
        return;
    };
    defer allocator.free(buff);

    var lines = std.mem.split(u8, buff, "\n");

    var list = std.ArrayList([]const u8).init(allocator);
    defer list.deinit();

    while (lines.next()) |line| {
        if (std.mem.eql(u8, line, "")) break;
        list.append(line) catch unreachable;
        // print("{s}\n", .{line});
    }

    // print("{s}", .{list.items});

    if (args.func == 0) {
        task0(list) catch {};
    } else {
        task1(list) catch {};
    }
}

fn task0(list: std.ArrayList([]const u8)) !void {
    // print("{}\n", .{list.items.len});
    var safe: u64 = 0;

    blk: for (list.items) |line| {
        var it = std.mem.splitSequence(u8, line, " ");
        var current = try parseInt(i64, it.next().?, 10);
        var next = try parseInt(i64, it.next().?, 10);
        const increasing: bool = if (current < next) true else false;
        var diff = if (increasing) next - current else current - next;

        if (diff < 1 or diff > 3) {
            continue :blk;
        }
        current = next;

        while (it.next()) |entry| {
            next = try parseInt(i64, entry, 10);
            diff = if (increasing) next - current else current - next;
            if (diff < 1 or diff > 3) {
                continue :blk;
            }
            current = next;
        }
        safe += 1;

        //print("{} {} {}\n", .{ current, next, total });
    }
    print("{}", .{safe});
}

fn valid_range(increasing: bool, left: i64, right: i64) bool {
    const val = if (increasing) right - left else left - right;
    return 0 < val and val < 4;
}

fn valid(list: []i64, ignore: usize) bool {
    var index: u64 = 0;
    if (index == ignore) {
        index += 1;
    }
    var current = list[index];
    index += 1;

    if (index == ignore) {
        index += 1;
    }
    const next = list[index];
    index += 1;

    const increasing = if (next > current) true else false;
    if (!valid_range(increasing, current, next)) {
        return false;
    }
    current = next;

    for (list[index..], index..) |item, i| {
        if (i == ignore) {
            continue;
        }
        if (!valid_range(increasing, current, item)) {
            return false;
        }
        current = item;
    }
    return true;
}

fn task1(list: std.ArrayList([]const u8)) !void {
    var safe: u64 = 0;

    blk: for (list.items) |line| {
        var it = std.mem.splitSequence(u8, line, " ");

        var array = std.ArrayList(i64).init(allocator);
        defer array.deinit();

        while (it.next()) |item| {
            try array.append(try parseInt(i64, item, 10));
        }
        for (0..array.items.len) |ignore| {
            if (valid(array.items, ignore)) {
                safe += 1;
                continue :blk;
            }
        }
    }
    print("{}", .{safe});
}
