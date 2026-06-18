class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_preq = defaultdict(set)
        course_unlocks = defaultdict(set)

        for courses in prerequisites:
            course_preq[courses[0]].add(courses[1])
            course_unlocks[courses[1]].add(courses[0])
        
        queue = deque()
        exam_done = set()

        for course in range(numCourses):
            if course not in course_preq:
                queue.append(course)

        while queue:
            exam = queue.popleft()
            exam_done.add(exam)

            for next_exam in course_unlocks[exam]:
                course_preq[next_exam].discard(exam)
                if not course_preq[next_exam]:
                    queue.append(next_exam)



        return len(exam_done) == numCourses

        



        