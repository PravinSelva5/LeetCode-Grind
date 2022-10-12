class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        lightest_person = 0
        heaviest_person = len(people) - 1

        boats = 0

        while heaviest_person >= lightest_person:
            if lightest_person == heaviest_person:
                boats += 1
                break
            if people[heaviest_person] + people[lightest_person] <= limit:
                heaviest_person -= 1
            boats += 1
            heaviest_person -= 1

        return boats
