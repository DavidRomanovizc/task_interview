def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def get_intersection(intervals1, intervals2):
    intersections = []
    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        start = max(intervals1[i][0], intervals2[j][0])
        end = min(intervals1[i][1], intervals2[j][1])
        if start < end:
            intersections.append([start, end])

        if intervals1[i][1] < intervals2[j][1]:
            i += 1
        else:
            j += 1
    return intersections


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_intervals = [[intervals['lesson'][0], intervals['lesson'][1]]]
    pupil_intervals = [[intervals['pupil'][i], intervals['pupil'][i + 1]] for i in range(0, len(intervals['pupil']), 2)]
    tutor_intervals = [[intervals['tutor'][i], intervals['tutor'][i + 1]] for i in range(0, len(intervals['tutor']), 2)]

    pupil_intervals = merge_intervals(pupil_intervals)
    tutor_intervals = merge_intervals(tutor_intervals)

    pupil_lesson_intersection = get_intersection(lesson_intervals, pupil_intervals)
    tutor_lesson_intersection = get_intersection(lesson_intervals, tutor_intervals)

    common_intersection = get_intersection(pupil_lesson_intersection, tutor_lesson_intersection)

    total_time = sum(end - start for start, end in common_intersection)
    return total_time
