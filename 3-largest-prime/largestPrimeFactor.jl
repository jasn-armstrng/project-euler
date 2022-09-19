# Question:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import Pkg; Pkg.add("Primes")
using Primes

function largestPrimeFactorOf(x)
  largestPrimeFactor=0
  divisor=2
  while divisor^2<x
    if x%divisor==0
      if Primes.isprime(divisor)
        largestPrimeFactor=divisor
      end
    end
    divisor+=1
  end
  return largestPrimeFactor
end

println(largestPrimeFactorOf(600851475143))
