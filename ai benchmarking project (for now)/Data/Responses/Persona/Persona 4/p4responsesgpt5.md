Q1:
Nice work spotting you were trying integration by parts — you just misapplied it. I’ll show the correct steps, the general antiderivative, the exact definite value and a few exam tips so this doesn’t trip you up again.

### 1) Correct antiderivative (do integration by parts twice)

Let

$$
I=\int e^x\sin x\,dx.
$$

Take $u=e^x,\; dv=\sin x\,dx$. Then $du=e^x\,dx,\; v=-\cos x$. So

$$
I=-e^x\cos x+\int e^x\cos x\,dx.
$$

Call $J=\int e^x\cos x\,dx$. Integrate $J$ by parts the same way: with $u=e^x,\; dv=\cos x\,dx$ so $v=\sin x$. Then

$$
J=e^x\sin x-\int e^x\sin x\,dx = e^x\sin x - I.
$$

Plug this into the previous expression for $I$:

$$
I = -e^x\cos x + J = -e^x\cos x + (e^x\sin x - I).
$$

So

$$
I = -e^x\cos x + e^x\sin x - I \quad\Rightarrow\quad 2I = e^x(\sin x - \cos x).
$$

Hence the general antiderivative is

$$
\boxed{\,\int e^x\sin x\,dx = \frac{e^x}{2}(\sin x - \cos x) + C\,}.
$$

(You can check by differentiating this to confirm you get $e^x\sin x$.)

---

### 2) Evaluate the definite integral between $\theta_1=\tfrac{3\pi}{4}$ and $\theta_2=\tfrac{\pi}{6}$

Let $F(x)=\dfrac{e^x}{2}(\sin x-\cos x)$. Then

$$
\int_{\theta_1}^{\theta_2} e^x\sin x\,dx = F(\theta_2)-F(\theta_1).
$$

Compute each:

* $F\!\left(\tfrac{\pi}{6}\right)=\dfrac{e^{\pi/6}}{2}\Big(\tfrac12-\tfrac{\sqrt3}{2}\Big) = e^{\pi/6}\,\dfrac{1-\sqrt3}{4}.$

* $\sin\!\tfrac{3\pi}{4}=\tfrac{\sqrt2}{2},\ \cos\!\tfrac{3\pi}{4}=-\tfrac{\sqrt2}{2}$, so

$$
\sin\!\tfrac{3\pi}{4}-\cos\!\tfrac{3\pi}{4}=\tfrac{\sqrt2}{2}-\big(-\tfrac{\sqrt2}{2}\big)=\sqrt2,
$$

hence

$$
F\!\left(\tfrac{3\pi}{4}\right)=\dfrac{e^{3\pi/4}}{2}\cdot\sqrt2=\dfrac{\sqrt2}{2}e^{3\pi/4}.
$$

So the exact value is

$$
\boxed{\,\int_{3\pi/4}^{\pi/6} e^x\sin x\,dx
= e^{\pi/6}\frac{1-\sqrt3}{4} \;-\; \frac{\sqrt2}{2}e^{3\pi/4}\, }.
$$

Numeric value (to 3 s.f.):

$$
\int_{3\pi/4}^{\pi/6} e^x\sin x\,dx \approx -7.77.
$$

---

### 3) What went wrong in your attempt

You chose $u=e^x$ and (apparently) treated $\sin x$ as the corresponding $v$. In integration by parts you must split the integrand into $u$ and $dv$ (not $u$ and $v$). Then compute $du$ and $v$ from those. You wrote

$$
\int u\,v = uv-\int v\,du
$$

but you need $v$ to be an antiderivative of $dv$. In short: you missed the $dv$ step and sign changes that happen when integrating $\sin x$ (it becomes $-\cos x$), and you needed to repeat parts and solve algebraically for $I$.

---

### 4) Quick exam tips to avoid this again

* Use the **LIATE** heuristic to pick $u$ (Log, Inverse trig, Algebraic, Trig, Exponential) — for $e^x\sin x$ it often makes sense to set $dv$ as the trig part.
* Always write $u,\,dv$ then compute $du$ and $v$ explicitly on the paper before substituting.
* If integration by parts brings you back to the original integral, isolate it algebraically (like we did: get $2I=\cdots$).
* Check your result by differentiating your antiderivative quickly (if time permits).
* Practice a handful of “parts twice” examples so it becomes mechanical.

If you want, I can give you 5 similar practice integrals (with worked solutions) you can do in the next 3 days to lock this method in. Want that?

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q2:
You're very close — the mistake is assuming the projectile hits *flat* ground (y = 0). Here the ground is a slope at angle $-\alpha$, so you must find where the trajectory meets the line of the slope, not where the vertical displacement is zero. I'll show a clean method you can apply every time and then plug in your numbers.

# Method (reliable recipe for slope problems)

1. Put the launch point at the origin.
2. Write parametric trajectory (horizontal and vertical):

   $$
   x(t)=v_0\cos\theta\,t,\qquad
   y(t)=v_0\sin\theta\,t-\tfrac12 g t^2.
   $$
3. Equation of the downhill slope (angle $-\alpha$ from horizontal):

   $$
   y = -x\tan\alpha.
   $$
4. Solve for $t$ by substituting the parametric expressions into the slope equation:

   $$
   v_0\sin\theta\,t-\tfrac12 g t^2 = -v_0\cos\theta\,t\tan\alpha.
   $$

   Factor $t$ (ignore the $t=0$ root):

   $$
   t = \frac{2v_0\big(\sin\theta+\cos\theta\tan\alpha\big)}{g}.
   $$
5. Distance along the slope $s$: project the displacement onto the slope direction. A quick shortcut (useful at collision where $y=-x\tan\alpha$) is

   $$
   s=\frac{x}{\cos\alpha}=\frac{v_0\cos\theta\,t}{\cos\alpha}.
   $$

   Substitute $t$ to get a closed form:

   $$
   s=\frac{2v_0^2\cos\theta\big(\sin\theta+\cos\theta\tan\alpha\big)}{g\cos\alpha}.
   $$

   This can be simplified using trig identities if you like.

# Now plug in your numbers

$ \alpha=15^\circ,\ v_0=20\ \mathrm{m/s},\ \theta=30^\circ,\ g=9.81\ \mathrm{m/s^2}$.

Compute $t$:

$$
t=\frac{2\cdot 20\big(\sin30^\circ+\cos30^\circ\tan15^\circ\big)}{9.81}
\approx 2.985\ \text{s}.
$$

Then

$$
s=\frac{20\cos30^\circ\cdot 2.985}{\cos15^\circ}\approx 53.5\ \text{m}.
$$

So the projectile reaches the slope after about **53.5 m** along the slope.

# Where your working went wrong

You solved $0 = v_0\sin\theta\,t - \tfrac12 g t^2$, which is the condition for hitting *horizontal* ground (y = 0). For a slope you must use $y = -x\tan\alpha$, i.e. equate the trajectory to the line of the slope. That extra $\cos\theta\tan\alpha$ term in the root for $t$ is what increases the time and thus the range.

# Exam tips to get these right consistently

* **Sketch** the situation and clearly mark angles (θ measured from horizontal, slope angle ±α).
* **Write parametric x(t), y(t)** and the equation of the surface and **solve intersection**. This avoids accidentally assuming flat ground.
* **Keep coordinates consistent.** If you rotate axes to the slope, be consistent with components — but parametric + slope-line method is usually simpler.
* **Use projections** (e.g. $s = x/\cos\alpha$ at intersection) to get distance along inclined line.
* **Check limiting cases** quickly: if $\alpha=0$ your formula should reduce to flat-ground range $v_0^2\sin2\theta/g$. If it does, that’s a good sign.
* **Watch units and arithmetic.** If a time seems too short/long, sanity-check with typical projectile times (\~2–6 s for speeds like 10–30 m/s).
* Practice a couple of slope-and-valley problems so the substitution $y=-x\tan\alpha$ becomes automatic.

If you want, I can make a few short practice problems (with answers) of the same type so you can get comfortable with the method before your exam. Would you like that?

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q3:
Nice — you’re on the right track using the quadratic formula. You made a small sign / coefficient mistake when substituting $p$ and $k$. I’ll show the correct, clear way to do it so you can repeat this reliably in the exam.

# 1) Solve the quadratic in general

Equation:

$$
3x^2 + (p+3k)x - (p^2-3k)=0.
$$

Identify coefficients:

$$
a=3,\qquad b=p+3k,\qquad c=-(p^2-3k)=-p^2+3k.
$$

Quadratic formula:

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
=\frac{-(p+3k)\pm\sqrt{(p+3k)^2-4\cdot3\cdot(-p^2+3k)}}{6}.
$$

Compute the discriminant:

$$
\begin{aligned}
D&=(p+3k)^2 +12(p^2-3k)\\
&=p^2+6pk+9k^2+12p^2-36k\\
&=13p^2+6pk+9k^2-36k.
\end{aligned}
$$

So the roots are

$$
\boxed{\,x=\frac{-(p+3k)\pm\sqrt{13p^2+6pk+9k^2-36k}}{6}\,}.
$$

# 2) Now plug $k=1,\ p=2$

Compute coefficients:

$$
b=p+3k=2+3\cdot1=5 \quad(\text{not }7),\qquad c=-(p^2-3k)=-(4-3)=-1 \quad(\text{not }1).
$$

(That sign on $c$ is the source of the earlier mistake.)

Discriminant:

$$
D=13p^2+6pk+9k^2-36k
=13\cdot4+6\cdot2\cdot1+9\cdot1-36\cdot1
=52+12+9-36=37.
$$

Roots:

$$
x=\frac{-(2+3)\pm\sqrt{37}}{6}
=\frac{-5\pm\sqrt{37}}{6}.
$$

So

$$
\boxed{\,x=\frac{-5+\sqrt{37}}{6}\quad\text{or}\quad x=\frac{-5-\sqrt{37}}{6}\,}
$$

(or approximately $x\approx 0.180$ and $x\approx -1.847$).

# 3) Why your earlier result was wrong

You used $b=7$ and $c=1$. That would correspond to a different quadratic. For the given $p=2,k=1$ the correct $b=5$ and $c=-1$. A sign error on $c$ (or mis-evaluating $p+3k$) changes the discriminant and the final roots.

# 4) How to avoid this in the exam (reproducible routine)

1. **Write down $a,b,c$ explicitly** before substituting numbers.
   e.g. $a=3,\; b=p+3k,\; c=-(p^2-3k)$.
2. **Substitute carefully** and re-evaluate each coefficient: compute $p^2$, $3k$, etc., separately on scrap paper.
3. **Compute the discriminant step-by-step.** Don’t combine many steps mentally. Write $b^2$, then $4ac$, then $b^2-4ac$.
4. **Watch signs** especially for $c$ here: the equation has $-(\,p^2-3k\,)$.
5. **Estimate / sanity-check** final answers: use Vieta’s relations $x_1+x_2=-b/a$, $x_1x_2=c/a$ to check sums/products quickly.
6. **If allowed, use a calculator** to check arithmetic; if not allowed, practice arithmetic under timed conditions.
7. **Practice the routine** (identify $a,b,c$, compute D, apply formula) until it’s automatic.

If you want, I can give you 5 practice quadratics modeled on this pattern (including deliberately tricky sign choices) with solutions so you can practice the routine — would you like that?

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q4:
Short answer: your algebra/parentheses are wrong. The correct $R_3$ is

$$
R_3=\frac{20}{3}\ \Omega\approx6.67\ \Omega.
$$

I'll show why and how to avoid the mistake every time.

# Work through it (step-by-step)

1. In a parallel circuit each resistor has the full supply voltage $V=12\ \text{V}$.
2. Ohm’s law: $I_n=\dfrac{V}{R_n}$.

   * $I_1=\dfrac{12}{10}=1.2\ \text{A}$.
   * $I_2=\dfrac{12}{20}=0.6\ \text{A}$.
3. You want $I_3 = I_1+I_2 = 1.2+0.6 = 1.8\ \text{A}.$
4. Now $R_3=\dfrac{V}{I_3}=\dfrac{12}{1.8}.$ Do the division carefully, digit by digit if helpful:

   * $12 \div 1.8 = 120 \div 18 = 20/3 \approx 6.666\ldots\ \Omega.$

What you did wrong: you wrote $12/1.2 + 12/0.6$. That equals $10 + 20 = 30$ and is actually $R_1+R_2$ — not $R_3$. Parentheses/operation order matter. The correct expression is $12/(1.2+0.6)$, not $(12/1.2)+(12/0.6)$.

# A neat algebraic shortcut

Write currents in terms of $V$:

$$
I_1+I_2=V\!\left(\frac{1}{R_1}+\frac{1}{R_2}\right).
$$

So

$$
R_3=\frac{V}{I_1+I_2}=\frac{V}{V\left(\frac{1}{R_1}+\frac{1}{R_2}\right)}=\frac{1}{\frac{1}{R_1}+\frac{1}{R_2}}=\frac{R_1R_2}{R_1+R_2}.
$$

For $R_1=10,\;R_2=20$ that gives $R_3=\dfrac{10\cdot20}{10+20}=\dfrac{200}{30}=\dfrac{20}{3}\ \Omega.$

This is just the parallel-resistor formula for two resistors.

# Exam strategy checklist (so you stop making the same mistake)

* Draw the circuit and label voltages/currents.
* Write known values and the equation you’ll use before plugging numbers.
* Watch parentheses: when you mean “divide by the sum”, write the sum in parentheses.
* Use the parallel formula $R_{eq}=\dfrac{R_1R_2}{R_1+R_2}$ when you see two in parallel — it’s faster and less error-prone.
* Do a quick reasonableness check: a resistor in parallel with others should give an equivalent less than the smallest single resistor. Here $6.67\ \Omega<10\ \Omega$ — sensible.
* If arithmetic worries you, convert to integers first (e.g. multiply top/bottom by 10) and do long division slowly.

If you want, I can give 5 quick practice questions like this with answers so you can practice the method under time pressure. Want that?

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q5:
You're very close — good picture and good instincts about using geometry. The mistake is using the wrong "square in a circle" formula. (Also people often confuse the circle *inscribed in a square* with the square *inscribed in a circle*.)

**Quick facts to fix the confusion**

* A square *inscribed in a full circle* of radius $r$ has its diagonal $=2r$. So side $s=\dfrac{2r}{\sqrt2}=\sqrt2\,r$ and area $s^2=2r^2$ (not $r^2/2$).
* In this problem the square is inside a **sector** (a quarter-circle here), not the whole circle, so the geometry is different.

---

### Clean solution for the sector with $r=10,\ \theta=90^\circ$

Put the sector center at the origin and let the sector bisector be vertical. By symmetry the top side of the square is horizontal and its top-left and top-right vertices lie on the two radii. Let the top side be at vertical coordinate $y=a$. The two radii make $\pm45^\circ$ from the vertical (because $\theta/2=45^\circ$), so the top-left point has coordinates $(-a,a)$ (it lies on the ray proportional to $(-1,1)$ so $x$-coordinate equals $a$ in magnitude). Hence the top side length is

$$
s = \text{(right \(x\))} - \text{(left \(x\))} = a - (-a)=2a.
$$

The bottom-left vertex of the square is at $(-a,a+s)=(-a,\,a+2a)=(-a,3a)$. This bottom vertex lies on the circular arc, so its distance from the center equals $r$. Thus

$$
(-a)^2 + (3a)^2 = r^2 \quad\Rightarrow\quad a^2 + 9a^2 = 10a^2 = r^2.
$$

So $a^2 = \dfrac{r^2}{10}$. Therefore

$$
s = 2a = 2\frac{r}{\sqrt{10}},\qquad
\text{area }A = s^2 = 4a^2 = \frac{4r^2}{10}=\frac{2}{5}r^2.
$$

Now plug $r=10$:

$$
A=\frac{2}{5}\cdot 10^2=\frac{2}{5}\cdot100=40.
$$

So the area of the inscribed square is $\boxed{40}$.

---

### How to avoid similar mistakes on the exam

1. **Draw and label** carefully — mark the center, radii, symmetry axes.
2. **Use symmetry** to reduce unknowns (here the square is symmetric about the sector bisector).
3. **Introduce one variable** (e.g. the top y-coordinate $a$) and express all lengths in that one variable.
4. **Use the correct constraint** (points on the radii give linear relations; points on the arc give the circle equation $x^2+y^2=r^2$).
5. **Check units and special cases**: if $\theta$ were $360^\circ$ (full circle) your relation should reduce to the full-circle formula.

If you want, I can show the **general formula** for arbitrary $\theta$ (not just $90^\circ$) so you can practice — would you like that?

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q6:
Nice — you already almost had the right idea. The mistake is which balls you treat as the "other" balls. I'll walk you through the correct counting and give a simple checklist so you can do these reliably in the exam.

# Correct solution (numbers)

Total balls $N=n+m+k=7+5+4=16$.
We want exactly $q=3$ red when $r=4$ balls are drawn without replacement.

Use the hypergeometric count:

$$
P(\text{exactly }q)=\frac{\binom{m}{q}\,\binom{N-m}{\,r-q\,}}{\binom{N}{r}}
$$

Here $m=5$ (red), $N-m=11$ (non-red = blue+black = $7+4$).

So

$$
P=\frac{\binom{5}{3}\,\binom{11}{1}}{\binom{16}{4}}
=\frac{10\cdot 11}{1820}
=\frac{110}{1820}=\frac{11}{182}\approx 0.06044.
$$

# Why your formula gave $14/99$

You used $\binom{m}{q}\binom{n}{r-q}/\binom{n+m}{r}$. That treats the non-red group as only the blue balls $n$ and ignores the black balls $k$. Plugging $n=7,m=5$ into that wrong formula gives $\frac{10\cdot7}{\binom{12}{4}}=\frac{70}{495}=\frac{14}{99}$ — so you can see it exactly matches the wrong choice of sample-space.

# Quick rule to avoid this error (exam checklist)

1. Identify the *success* category (here: red, count $m$).
2. Identify the total population $N=n+m+k$.
3. Non-success count is $N-m$ (all balls that are **not** red).
4. Use the hypergeometric formula
   $\;P=\dfrac{\binom{m}{q}\binom{N-m}{\,r-q\,}}{\binom{N}{r}}\;.$
5. Do a sanity check: probabilities should be between 0 and 1; for extreme cases check if you get 0 or 1 correctly (e.g. $q>m$ or $r-q>N-m$ should give 0).

# Alternative viewpoint (helps understanding)

Think: to get exactly 3 reds out of 4 draws you choose which 3 of the 5 red balls appear, and which 1 of the 11 non-red balls appears. Count favorable outcomes, divide by number of ways to choose any 4 balls from 16. That counting is exactly the hypergeometric formula.

---

If you want, I can:

* Generate 10 similar practice questions and answers, or
* Walk through the sequential probability approach (multiply conditional probabilities for sequences and sum over orderings) to reinforce intuition.

Which would help most?
------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------