# Question:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

function sumOfMultiples(x, y; range=1)
  sum = 0
  for i = 1:range-1
    if i%x == 0 || i%y == 0
      sum += i
    end
  end
  return sum
end

println(sumOfMultiples(3, 5, range=1000))
# Measure performance with @time
@time sumOfMultiples(3, 5, range=1000)
