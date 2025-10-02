Q1:
Nice — you're on the right track thinking about symmetry, but here it doesn't apply. Let's do the integral step by step.

# Indefinite integral

Let

$$
I=\int e^x\sin x\,dx.
$$

Integrate by parts once with $u=\sin x$, $dv=e^x dx$ (so $du=\cos x\,dx$, $v=e^x$):

$$
I = e^x\sin x - \int e^x\cos x\,dx.
$$

Call the remaining integral $J=\int e^x\cos x\,dx$. Integrate $J$ by parts with $u=\cos x$, $dv=e^x dx$ ($du=-\sin x\,dx$, $v=e^x$):

$$
J = e^x\cos x - \int e^x(-\sin x)\,dx = e^x\cos x + \int e^x\sin x\,dx = e^x\cos x + I.
$$

Substitute $J$ back into the first equation:

$$
I = e^x\sin x - J = e^x\sin x - (e^x\cos x + I).
$$

So

$$
I = e^x\sin x - e^x\cos x - I \quad\Rightarrow\quad 2I = e^x(\sin x - \cos x).
$$

Hence

$$
\boxed{\displaystyle \int e^x\sin x\,dx = \frac{e^x}{2}(\sin x-\cos x)+C.}
$$

(You can check by differentiating the right-hand side; it indeed gives $e^x\sin x$.)

# Definite integral $\displaystyle\int_{0}^{\pi} e^x\sin x\,dx$

Use the antiderivative $F(x)=\tfrac{e^x}{2}(\sin x-\cos x)$. Then

$$
\int_{0}^{\pi} e^x\sin x\,dx = F(\pi)-F(0).
$$

Evaluate:

* $F(\pi)=\tfrac{e^\pi}{2}(\sin\pi-\cos\pi)=\tfrac{e^\pi}{2}(0-(-1))=\tfrac{e^\pi}{2}.$
* $F(0)=\tfrac{e^0}{2}(\sin0-\cos0)=\tfrac{1}{2}(0-1)=-\tfrac{1}{2}.$

So

$$
\boxed{\displaystyle \int_{0}^{\pi} e^x\sin x\,dx=\frac{e^\pi}{2}-\left(-\frac{1}{2}\right)=\frac{e^\pi+1}{2}.}
$$

Numeric approx: $e^\pi\approx 23.1407$, so the integral is about $12.0703$.

# About your odd-function thought

* A function being *odd* (so its integral over $[-a,a]$ is zero) requires $f(-x)=-f(x)$ and symmetric limits $[-a,a]$.
* Here $e^x\sin x$ is **not** odd (because of the $e^x$ factor), and the limits $0$ to $\pi$ are not symmetric about $0$.
* The fact that $\sin0=\sin\pi=0$ only means the integrand is zero at the endpoints — it doesn't make the whole area zero.

If you'd like, I can show the complex-exponential method (using $e^{(1+i)x}$) or plot the integrand to build more intuition. Want that? 😊

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q2:
Nice — welcome back to projectile fun! 🎯 You're on the right track with the SUVAT idea, but a small correction: the kinematic formula you want is

$$
s = ut + \tfrac{1}{2}at^2,
$$

with the $t^2$ on the acceleration term.

For the given special case $\alpha=0^\circ$ the slope is horizontal, so this is the standard range problem (launch and landing at the same elevation). I'll show a short, clear derivation and plug in the numbers.

# Derivation (short)

Initial speed $v_0=20\ \mathrm{m/s}$, launch angle $\theta=30^\circ$.
Resolve velocities:

$$
v_{x}=v_0\cos\theta,\qquad v_{y}=v_0\sin\theta.
$$

Time of flight (vertical motion — lands at same height):

$$
0 = v_y t - \tfrac12 g t^2 \quad\Rightarrow\quad t=\frac{2v_y}{g}=\frac{2v_0\sin\theta}{g}.
$$

Range along horizontal (distance along slope since slope is horizontal):

$$
R = v_x t = v_0\cos\theta\cdot\frac{2v_0\sin\theta}{g}=\frac{v_0^2\sin(2\theta)}{g}.
$$

# Plug in numbers

$\sin(2\theta)=\sin(60^\circ)=\sqrt{3}/2$. Using $g=9.81\ \mathrm{m/s^2}$,

$$
R=\frac{20^2\cdot\sin 60^\circ}{9.81}
=\frac{400\cdot(\sqrt{3}/2)}{9.81}
\approx 35.31\ \text{m}.
$$

You can also see it stepwise:

* $v_y=v_0\sin30^\circ=20\times0.5=10\ \mathrm{m/s}$.
* Time of flight $t=2\cdot10/9.81\approx2.039\ \mathrm{s}$.
* $v_x=20\cos30^\circ=20\tfrac{\sqrt3}{2}\approx17.3205\ \mathrm{m/s}$.
* Range $R=v_x t\approx17.3205\times2.039\approx35.31\ \mathrm{m}$.

So the projectile travels **≈ 35.31 m** along the (horizontal) slope before first contact.

If you want, I can:

* show the algebra in more detail, or
* solve the general case with a slope inclined at angle $-\alpha$ (nonzero $\alpha$), or
* plot the trajectory so you can visualise it.

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q3:
Nice — you remembered the right idea (the quadratic formula) but slipped on a parentheses / square-root step. Let’s do it cleanly step-by-step.

### 1. Identify $a,b,c$

For

$$
3x^2+(p+3k)x-(p^2-3k)=0
$$

we have

$$
a=3,\qquad b=p+3k,\qquad c=-(p^2-3k)=-p^2+3k.
$$

### 2. Quadratic formula (correct form)

The correct formula is

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

**Note:** it’s $\sqrt{\,b^2-4ac\,}$, not $b^2-4ac$ without the square root.

### 3. Compute the discriminant

$$
\Delta=b^2-4ac=(p+3k)^2-4\cdot 3\cdot(-p^2+3k)
=(p+3k)^2+12(p^2-3k).
$$

Expanding gives

$$
\Delta=13p^2+6pk+9k^2-36k.
$$

### 4. General roots

$$
\boxed{\,x=\dfrac{-(p+3k)\pm\sqrt{\,13p^2+6pk+9k^2-36k\,}}{6}\,}
$$

---

### 5. Now the specific case $k=0,\ p=1$

Substitute $k=0,\ p=1$:

* $a=3,\ b=1,\ c=-(1^2-0)=-1$.
* Discriminant: $\Delta=13$.

So the roots are

$$
x=\frac{-1\pm\sqrt{13}}{6}.
$$

Exact roots:

$$
x_1=\frac{-1+\sqrt{13}}{6},\qquad x_2=\frac{-1-\sqrt{13}}{6}.
$$

Decimal approximations:

$$
x_1\approx\frac{-1+3.605551}{6}\approx0.434259,\qquad
x_2\approx\frac{-1-3.605551}{6}\approx-0.767592.
$$

Both are real and distinct because $\Delta=13>0$.

### 6. Quick verification (plugging back)

If you substitute $x_1$ or $x_2$ into $3x^2+x-1$ you will get (within rounding) zero — that’s the guarantee from the quadratic formula. Numerically:

* For $x_1\approx0.434259$: $3x_1^2+x_1-1\approx0.000000$ (rounding).
* For $x_2\approx-0.767592$: likewise $\approx0.000000$.

### 7. Why you were getting 2 or $-7/3$

A common mistake is forgetting the square root in the formula (writing $-b\pm(b^2-4ac)\over 2a$ instead of $-b\pm\sqrt{b^2-4ac}\over 2a$), or mis-signing $c$. Those incorrect roots you found do not satisfy the equation — when you plug them in you get $13$, not $0$ (which shows the calculation was off).

---

If you want, I can show the step where someone who forgets the square root ends up with the wrong numbers, or walk through a couple more practice problems with you so this gets comfortable. Nice work catching the mismatch when you plugged the roots back in — that’s the right way to debug! 👏

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q4:
Nice — welcome back to circuits! You're very close on the ideas but mixed up series vs parallel. I’ll walk you through it simply.

### Key idea

For resistors in **parallel** the voltage across each resistor is the same (here $V=12\ \text{V}$). So the current through each resistor is given directly by Ohm’s law applied to that resistor:

$$
I_n=\frac{V}{R_n}.
$$

### Compute each current (digit-by-digit)

* $I_1=\dfrac{12}{10}=1.2\ \text{A}.$
* $I_2=\dfrac{12}{20}=0.6\ \text{A}.$
* $I_3=\dfrac{12}{15}=0.8\ \text{A}.$

So the currents are $1.2\ \text{A},\ 0.6\ \text{A},\ 0.8\ \text{A}$ through $R_1,R_2,R_3$ respectively.

### Total current and equivalent resistance

Total current (sum of branch currents):

$$
I_{\text{tot}}=1.2+0.6+0.8=2.6\ \text{A}.
$$

Equivalent resistance $R_{\text{eq}}$ of the parallel network:

$$
\frac{1}{R_{\text{eq}}}=\frac{1}{10}+\frac{1}{20}+\frac{1}{15}
=0.1+0.05+\tfrac{1}{15}
=0.216666\ldots=\frac{13}{60},
$$

so

$$
R_{\text{eq}}=\frac{60}{13}\approx 4.6154\ \Omega.
$$

Check: $V=I_{\text{tot}}R_{\text{eq}} \Rightarrow 12\approx 2.6\times 4.6154$ — it matches.

### Why the other approach was wrong

You added the resistances (that’s the rule for **series** resistors). In parallel, resistances **do not** add; conductances (or reciprocals of resistances) add. Also currents in parallel split **inversely** with resistance (lower resistance → more current), not in the same fraction as the resistances.

If you want, I can show a quick diagram or a couple more practice problems like this.

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q5:
Nice — you’re doing it right by starting with the square area. Let me walk you through a clean coordinate argument.

1. Area → side.
   The square’s area is $s^2=8$, so the side length is

   $$
   s=\sqrt{8}=2\sqrt2.
   $$

2. Put the sector center at the origin and take the two radii as the lines $y=x$ and $y=-x$ (a symmetric $90^\circ$ sector).
   If the square is centered left–right, its top side endpoints are $(-s/2,-s/2)$ and $(+s/2,-s/2)$ (these lie on $y=x$ and $y=-x$, respectively). So the top-right vertex is

   $$
   \Big(\tfrac{s}{2},-\tfrac{s}{2}\Big).
   $$

3. Distance from the center to that top-right vertex.
   Compute the radial distance $x$:

   $$
   x=\sqrt{\Big(\tfrac{s}{2}\Big)^2+\Big(-\tfrac{s}{2}\Big)^2}
    =\sqrt{2\cdot\Big(\tfrac{s}{2}\Big)^2}
    =\frac{s}{\sqrt2}.
   $$

   Substitute $s=2\sqrt2$:

   $$
   x=\frac{2\sqrt2}{\sqrt2}=2.
   $$

So the distance from the circle center to the top-right vertex of the square is $\boxed{2\ \text{m}}$.

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q6:
Nice — this is a perfect hypergeometric problem. Short answer first:

$$
\Pr(\text{exactly 2 red in 3 draws})=\frac{\binom{3}{2}\binom{5}{1}}{\binom{8}{3}}=\frac{15}{56}\approx0.267857\ (\approx26.79\%).
$$

Now the reasoning and why your initial idea was slightly off.

**Why not** just do $(3/8)(3/8)(5/8)$?
That treats each draw as if the probabilities stayed the same (as in sampling **with replacement**). Here we draw **without replacement**, so probabilities change after each draw. For example, if the first draw is red the probability the next is red is $2/7$, not $3/8$.

**Order-by-order (tree) method — one way to see it**
Take the specific order Red–Red–Blue. Its probability is

$$
\frac{3}{8}\cdot\frac{2}{7}\cdot\frac{5}{6}
= \frac{3\cdot2\cdot5}{8\cdot7\cdot6}
= \frac{30}{336} = \frac{5}{56}.
$$

There are $\binom{3}{2}=3$ different orders that have exactly two reds and one blue (RRB, RBR, BRR), each with the same probability, so total probability is

$$
3\cdot\frac{5}{56}=\frac{15}{56}.
$$

**Compact combinatorial formula (hypergeometric)**
Pick which 2 of the 3 reds are chosen: $\binom{3}{2}$. Pick which 1 of the 5 blues is chosen: $\binom{5}{1}$. Divide by the number of ways to pick any 3 balls from the 8 total: $\binom{8}{3}$. So

$$
\Pr=\frac{\binom{3}{2}\binom{5}{1}}{\binom{8}{3}}
=\frac{3\cdot5}{56}=\frac{15}{56}\approx0.267857.
$$

Your idea of multiplying by 3 (to account for ordering) was on the right track — the main mistake was using $3/8$ for the second red instead of $2/7$. Your final decimal (about 0.26) was close because of that — the exact value is $15/56\approx0.26786$.

Want a couple more practice problems (gradually harder) and we can walk through them together?

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------