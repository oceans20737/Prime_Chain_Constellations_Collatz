====================================================================
README: Constellations of Prime Chains on a Logarithmic Spiral
====================================================================
Author: Hiroshi Harada
Date: March 8, 2026

Overview
--------
This project provides a Python-based visualization tool that reveals
the geometric symmetries hidden within seemingly chaotic “prime chains.”

In a polar coordinate system using natural logarithms, each number is
plotted with radius r = ln(n) and angle θ = 2π ln(n). In this logarithmic
space, the growth rate of the recurrence relation directly determines
the shape of the figure. When n is multiplied by approximately c, the
angular displacement becomes:

    Δθ ≈ 2π ln(c)

Because ln(c) happens to be extremely close to a rational number p/q,
the sequence completes nearly p rotations in q steps. This produces
self-similar expanding figures (“constellations”) that approximate
beautiful geometric shapes such as triangles and pentagrams.

Featured Constellations
-----------------------
1. The Cunningham Triangle
   - Recurrence: n → 2n ± 1
   - Geometry: The growth rate is approximately 2.
     Since ln(2) ≈ 0.693 is close to 2/3, the sequence rotates about
     two full turns (4π) every three steps, forming a self-similar
     expanding “triangle.”
   - Included Data: Two of the world’s longest known Cunningham chains
       * Length-17 (1st kind)
       * Length-19 (2nd kind)

2. The Collatz Pentagram
   - Recurrence: n → (3n + 1) / 2 (applied only when the result is prime)
   - Geometry: The growth rate is approximately 1.5.
     Since ln(1.5) ≈ 0.405 is close to 2/5, the sequence rotates about
     two full turns (4π) every five steps, generating an expanding
     pentagram whose trajectory intersects itself.
   - Included Data: Newly discovered Collatz-type prime chains
       * Length-8: n0 = 44102911
       * Length-9: n0 = 35014031359

Search Results & Lower Bound
----------------------------
Using the ultra-fast multiple-precision library gmpy2, a full search
was executed up to an upper bound of 10^12. No Collatz-type prime
chains of length 10 (L10) or greater were found below this bound.
This provides an important lower bound for future explorations.

Usage
-----
Run the included Python scripts to render these celestial maps of
numbers. You may substitute the default arrays with your own discovered
prime chains to observe their unique geometric signatures.

License
-------
© 2026 Hiroshi Harada — MIT License.
This work and the accompanying code are licensed under the MIT License.
