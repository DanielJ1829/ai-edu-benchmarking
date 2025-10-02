# Benchmark Questions

This file contains the six benchmark math/physics questions, each in a **general form** with **three difficulty levels**.  
- **Level 1:** Direct numeric evaluation, simple parameters.  
- **Level 2:** Intermediate difficulty, more general setup.  
- **Level 3:** General case / extension (usually tackled by Persona 2, the confident & correct student).  

---

## Q1. Integral of $e^x \sin(x)$

**General form:**  
Evaluate  
$$
I = \int e^x \sin(x)\,dx
$$ 
and extend to definite integrals over given limits.

- **Level 1:** Evaluate $\int_0^\pi e^x \sin(x)\, dx$.  
- Expected solution: $I = \tfrac{1}{2}(1 + e^\pi)$
- **Level 2:** Find the general antiderivative, then evaluate for limits $\theta_1 = \tfrac{3\pi}{4}, \theta_2 = \tfrac{\pi}{6}$.  
- Expected solution: $I = \tfrac{1}{2}\big(e^{3\pi/4}(\sin(3\pi/4) - \cos(3\pi/4)) - e^{\pi/6}(\sin(\pi/6) - \cos(\pi/6))\big)$.
- **Level 3 (Persona 2):** Solve generally. Then evaluate for limits $\theta_1 = \tfrac{\pi}{8}, \theta_2 = -\tfrac{\pi}{4}$. Explore connections to $\int e^x \cos(x)\,dx$ and related integrals.  
- Expected solution: Antiderivative $F(x) = \tfrac{1}{2} e^x(\sin x - \cos x)$; definite integral $I = \tfrac{1}{2}\big(e^{\pi/8}(\sin(\pi/8) - \cos(\pi/8)) - e^{- \pi/4}(\sin(-\pi/4) - \cos(-\pi/4))\big)$.

---

## Q2. Projectile Motion Down a Slope

**General form:**  
A projectile is launched with initial speed $v_0$ at an angle $\theta$ above the horizontal, down a slope inclined at angle $-\alpha$. Assume no air resistance. Determine the distance travelled along the slope before the first point of contact.

- **Level 1:** $\alpha = 0^\circ,\ v_0 = 20\ \text{m/s},\ \theta = 30^\circ$.
- Expected solution: Range $R \approx 35.3\ \text{m}$.
- **Level 2:** $\alpha = 15^\circ,\ v_0 = 20\ \text{m/s},\ \theta = 30^\circ$.  
- Expected solution: Range $R \approx 30.6\ \text{m}$. 
- **Level 3:** Derive the general formula in terms of $v_0, \alpha, \theta$. Then determine the optimal $\theta$ for maximum distance.  
- Expected solution: $R = \tfrac{2 v_0^2 \cos\theta \sin(\theta + \alpha)}{g \cos^2\alpha}$; optimal $\theta = \tfrac{\pi}{4} - \tfrac{\alpha}{2}$.
---

## Q3. Polynomial Roots

**General form:**  
Solve the quadratic equation  
$
3x^2 + (p+3k)x - (p^2-3k) = 0
$  
and study the root behavior.

- **Level 1:** Solve explicitly for $p=1, k=2$.  
- Expected solution: Roots $x = 1,\ -\tfrac{5}{3}$.  
- **Level 2:** Set $k=0$. Solve in terms of $p$. For which values of $p$ do the roots differ in sign?
 - Expected solution: Roots $x = \tfrac{-p \pm \sqrt{p^2 + 12p}}{6}$. Signs differ for $p \in (-12, 0)$.
- **Level 3:** Solve the general case (arbitrary $p,k$), analyze discriminant and conditions for real/complex roots.  
- Expected solution: Equivalent $I_3$ requires $R_3 = \tfrac{R}{1 - (1/2)^{n-1}}$.

---

## Q4. Parallel Resistive Circuit

**General form:**  
An electric circuit with supply $V=12\ \text{V}$ has three resistors $R_1, R_2, R_3$ connected in parallel. Find current distributions and equivalent resistances under different conditions.

- **Level 1:** $R_1 = 10\ \Omega,\ R_2 = 20\ \Omega,\ R_3 = 15\ \Omega.$ Find the current through each resistor.
- Expected solution: $I_1 = 1.2\ \text{A},\ I_2 = 0.6\ \text{A},\ I_3 = 0.8\ \text{A}$.
- **Level 2:** $R_1 = 10\ \Omega,\ R_2 = 20\ \Omega.$ Determine $R_3$ such that $I_1 + I_2 = I_3.$  
- Expected solution: $R_3 = 6.67\ \Omega$.
- **Level 3 (Persona 2):** Extend Level 2: for $n$ resistors with $R_{i+1} = 2R_i$, determine conditions on $R_3$ such that its current equals the sum of all others. Explore the geometric series structure.  
- Expected solution: Equivalent $I_3$ requires $R_3 = \tfrac{R}{1 - (1/2)^{n-1}}$.
---

## Q5. Square Inscribed in a Circular Sector

**General form:**  
A square is inscribed inside a circular sector of radius $r$ and central angle $\theta$. Two vertices lie on the radii, two lie on the arc.

- **Level 1:** Square area = $8\ \text{m}^2$, sector angle $\theta = 90^\circ$. Find the distance between the top-right square vertex and the circle center.  
- Expected solution: Distance $\approx 3.36\ \text{m}$.
- **Level 2:** $r = 10,\ \theta = 90^\circ.$ Find the area of the inscribed square.  
- Expected solution: Square area $= 50\ \text{m}^2$.
- **Level 3 (Persona 2):** General case: derive the square’s area in terms of $r$ and $\theta$. Discuss general behavior and limiting cases. 
- Expected solution: $A = \dfrac{r^2 \sin^2(\tfrac{\theta}{2})}{1+\sin(\tfrac{\theta}{2})}$. 

---

## Q6. Probability of Drawing Balls

**General form:**  
A bag contains $n$ blue balls, $m$ red balls, and $k$ black balls. If $r$ balls are drawn without replacement, what is the probability that exactly $q$ of them are red?

- **Level 1:** $(n,m,k,r,q) = (5,3,0,3,2)$.  
- Expected solution: $P = \tfrac{\binom{3}{2}\binom{5}{1}}{\binom{8}{3}} = 0.357$.
- **Level 2:** $(n,m,k,r,q) = (7,5,4,4,3)$.  
- Expected solution: $P = \tfrac{\binom{5}{3}\binom{11}{1}}{\binom{16}{4}} \approx 0.103$.
- **Level 3 (Persona 2):** General case $(n,m,k,r,q)$. Extend Level 2: derive formula and analyze edge cases where the model breaks down (e.g., $q>r$, insufficient red balls, etc.).  
- Expected solution: $P = \dfrac{\binom{m}{q}\binom{n+k}{r-q}}{\binom{m+n+k}{r}}$, valid only if $q \le m$ and $q \le r$.