# Data Structures and numbers everyone should know
## Hashes
* Probability of at least one collision in Hash table: **`k^2/2N`**

  *k* - number of keys used, *N* - key space cardinality (assumption of ideal Uniform hash function)
  
  Example: k = 2^31, N = 2^32 (2 billions of keys in 4 billion key space) => Pcol = 0.5

* Avg number of collisions per key: **`k/N`**

  It follows Binomial distribution with `pmf(nt; k, p=1/N)` 
  
  *nt* - number of times a particular key would be drawn, *k* - as above, *N* - as above
  which in turn implies 
  
  `E[Nt] = k * 1/N = k/N`  - number of times a particular key is drawn in average across *k* draws.

* Avg number of collisions: **`k - N + N * ((N-1)/N)^k`**

 | k/N            | coll_num / k  |
 | -------------- |:-------------:|
 | 1.0            | 36%  |
 | 2^-2           | 20% |
 | 2^-3           | 10% |
 | 2^-3           | 6%  |
 | 2^-4           | 3%  |
 | 2^-5           | 1.5% |
