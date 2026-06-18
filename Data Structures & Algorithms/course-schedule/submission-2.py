class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_preq = [0] * numCourses
        course_unlocks = defaultdict(set)

        for courses in prerequisites:
            course_preq[courses[0]] += 1
            course_unlocks[courses[1]].add(courses[0])
        
        queue = deque()
        exam_done = set()

        for course in range(numCourses):
            if course_preq[course] == 0:
                queue.append(course)

        while queue:
            exam = queue.popleft()
            exam_done.add(exam)

            for next_exam in course_unlocks[exam]:
                course_preq[next_exam] -= 1
                if course_preq[next_exam] == 0 and next_exam not in exam_done:
                    queue.append(next_exam)

        return len(exam_done) == numCourses

        



        