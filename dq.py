from collections import deque
import itertools

class CheckDq:
	def movingAverage(self, iterable, n):

		elems_total = deque(iterable)
		result = []

		def logicImplement(local_elems_total, i):

			it = iter(local_elems_total)
			elems_sliced = deque(itertools.islice(it, n))
			avg_value = sum(elems_sliced)/i
			result.append(avg_value)
			visited_points = elems_sliced.popleft()
			local_elems_total.popleft()

			if len(local_elems_total) != i-1 :
				logicImplement(local_elems_total, i)

		logicImplement(elems_total, n)
		return result


if __name__ == '__main__':
	CallClass = CheckDq()
	# moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0)
	val = int(input())
	it_list = [40, 30, 50, 46, 39, 44]
	print(CallClass.movingAverage(it_list, val))