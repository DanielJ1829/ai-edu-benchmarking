Q1:
Nice work catching something felt off — you’re very close. The mistake is assuming an antiderivative is simply $-e^x\cos x$. That’s not the antiderivative of $e^x\sin x$. Let me show the correct method (integration by parts twice).

Set

$$
I=\int e^x\sin x\,dx.
$$

Integrate by parts with $u=\sin x,\;dv=e^xdx$. Then $du=\cos x\,dx,\;v=e^x$, so

$$
I = e^x\sin x - \int e^x\cos x\,dx.
$$

Call the remaining integral $J=\int e^x\cos x\,dx$. Integrate $J$ by parts with $u=\cos x,\;dv=e^xdx$; then $du=-\sin x\,dx,\;v=e^x$, so

$$
J = e^x\cos x + \int e^x\sin x\,dx = e^x\cos x + I.
$$

Plug this into the first equation:

$$
I = e^x\sin x - J = e^x\sin x - (e^x\cos x + I).
$$

So

$$
I = e^x\sin x - e^x\cos x - I \quad\Longrightarrow\quad 2I = e^x(\sin x - \cos x).
$$

Thus an antiderivative is

$$
I=\frac{1}{2}e^x(\sin x-\cos x)+C.
$$

Now evaluate the definite integral from $0$ to $\pi$:

$$
\int_0^\pi e^x\sin x\,dx
= \left.\frac{1}{2}e^x(\sin x-\cos x)\right|_0^\pi
= \frac{1}{2}e^\pi(0-(-1))-\frac{1}{2}e^0(0-1)
= \frac{e^\pi}{2} + \frac{1}{2}
= \frac{e^\pi+1}{2}.
$$

So the correct value is $\boxed{\dfrac{e^\pi+1}{2}}$. Numerically that’s about $12.0703$ (since $e^\pi\approx 23.1407$).

Quick check of your proposed antiderivative $-e^x\cos x$: differentiate it and you get

$$
\frac{d}{dx}[-e^x\cos x]=-e^x\cos x + e^x\sin x = e^x(\sin x-\cos x),
$$

which is not $e^x\sin x$. That’s exactly where the slip happened.

------------

Correctness:

Completeness:

Clarity:

Educational Value:

Tone/Coherence:

-----------

Q2:
Nice work catching something was off — your algebra step `t = 2u/g` is correct **only** when `u` is the *vertical* component of the initial velocity, not the total speed. You used the full speed $v_0=20\ \rm m/s$ there, which is the slip.

I'll show it cleanly.

1. vertical motion (take up positive):

$$
y(t)=v_{0}\sin\theta\ t-\tfrac12 g t^2.
$$

Projectile returns to launch height when $y(t)=0$. Factor $t\neq0$:

$$
v_{0}\sin\theta-\tfrac12 g t=0\quad\Rightarrow\quad
t=\frac{2v_{0}\sin\theta}{g}.
$$

Note $\sin30^\circ=0.5$, so the vertical component is $v_{0}\sin\theta=20\times0.5=10\ \rm m/s$. That gives

$$
t=\frac{2\cdot 10}{9.8}\approx2.0408\ \text{s}.
$$

2. horizontal motion (no horizontal acceleration):

$$
x(t)=v_{0}\cos\theta\ t,
$$

and for a horizontal ground ($\alpha=0^\circ$) the distance along the slope is the horizontal range $R=x(t)$. With $\cos30^\circ=\sqrt3/2$,

$$
R=v_{0}\cos\theta\ \frac{2v_{0}\sin\theta}{g}
=\frac{v_0^2\sin(2\theta)}{g}.
$$

Plug numbers:

$$
R=\frac{20^2\sin60^\circ}{9.8}
=\frac{400\times(\sqrt3/2)}{9.8}\approx 35.35\ \text{m}.
$$

Comparison with your number: you used $t=2u/g$ with $u=20$ (the full speed), giving $t\approx4.08$ s and then $20\times4.08\approx81.6$ m. That double-counted the speed — the time-of-flight formula uses the *vertical* component $v_0\sin\theta$, not the full $v_0$.

Final answer (for $\alpha=0^\circ,\ v_0=20\ \rm m/s,\ \theta=30^\circ$): **about 35.35 m** (≈35.4 m).

--------------
Correctness:

Completeness:

Clarity:

Educational Value:

Tone/Coherence:
-------------

Q3:
Great job writing things out carefully — let’s go step by step so we don’t slip anywhere.

We’re solving:

$$
3x^2 + (p+3k)x - (p^2-3k) = 0
$$

### Step 1. Identify coefficients

For a quadratic $ax^2 + bx + c = 0$:

* $a = 3$
* $b = p + 3k$
* $c = -(p^2 - 3k) = -p^2 + 3k$

### Step 2. Plug in $k=0,\ p=1$

Then:

* $a = 3$
* $b = 1 + 0 = 1$
* $c = -(1^2 - 0) = -1$

So the equation is:

$$
3x^2 + x - 1 = 0
$$

---

### Step 3. Use quadratic formula

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Here:

* $b^2 = 1^2 = 1$
* $4ac = 4 \cdot 3 \cdot (-1) = -12$
* So discriminant $= 1 - (-12) = 13$

Thus:

$$
x = \frac{-1 \pm \sqrt{13}}{2 \cdot 3} = \frac{-1 \pm \sqrt{13}}{6}
$$

---

### Step 4. Compare with your result

You had:

$$
x = -\tfrac{1}{6} + \tfrac{\sqrt{13}}{6}
$$

That’s **one** of the roots (the “+” case). The other root is

$$
x = -\tfrac{1}{6} - \tfrac{\sqrt{13}}{6}.
$$

---

✅ So your calculation was on the right track — you just forgot the “±” part, which gives two roots.

Would you like me to also go back and analyze **in general** how the roots behave depending on $k$ and $p$ (before substituting $k=0,\ p=1$)? That’s often what “study the root behavior” is asking.

--------------
Correctness:

Completeness:

Clarity:

Educational Value:

Tone/Coherence:
--------------

Q4:
Nice — you were close on the resistance but mixed up Ohm’s law when finding currents. Let me clean it up step-by-step.

**Given:** $V=12\ \text{V},\; R_1=10\ \Omega,\; R_2=20\ \Omega,\; R_3=15\ \Omega$.
Ohm’s law is $V=IR$ so $I=\dfrac{V}{R}$ (not $I=V\!R$).

### 1) Equivalent resistance

$$
\frac{1}{R_{\text{eq}}}=\frac{1}{R_1}+\frac{1}{R_2}+\frac{1}{R_3}
=\frac{1}{10}+\frac{1}{20}+\frac{1}{15}.
$$

Common denominator $60$: $\;6/60+3/60+4/60=13/60.$
So $\displaystyle R_{\text{eq}}=\frac{60}{13}\ \Omega\approx 4.61538\ \Omega.$

### 2) Total current from the supply

$$
I_{\text{total}}=\frac{V}{R_{\text{eq}}}
=\frac{12}{60/13}=12\cdot\frac{13}{60}=\frac{156}{60}=\frac{13}{5}=2.6\ \text{A}.
$$

### 3) Branch currents (each branch has the full 12 V across it)

$$
I_1=\frac{12}{10}=1.2\ \text{A},\qquad
I_2=\frac{12}{20}=0.6\ \text{A},\qquad
I_3=\frac{12}{15}=0.8\ \text{A}.
$$

Check: $1.2+0.6+0.8=2.6\ \text{A}=I_{\text{total}}$. Good.

### What went wrong in your work

* You used $I=V\!R$ instead of $I=\dfrac{V}{R}$. That’s why you got huge currents like 120 A etc.
* Your $R_{\text{eq}}=60/13\ \Omega$ was actually correct, but after that you multiplied instead of dividing when finding currents.

If you want, I can also compute the power dissipated in each resistor and total power drawn from the supply.

----------
Correctness:

Completeness:

Clarity:

Educational Value:

Tone/Coherence:
----------

Q5:
You're very close — the idea of using the $45^\circ$ symmetry is right, but the step $x = A\cos45^\circ$ is not valid because $A$ is an area (units $m^2$) while $x$ is a length (units $m$). You must convert the area to the square's side length first.

Here's a clean way to see it.

1. Square area $=8\Rightarrow$ side length

$$
s=\sqrt{8}=2\sqrt2.
$$

2. Put the sector center at the origin and let the sector be symmetric about the vertical. The right radius is the unit vector

$$
\mathbf{u}=\Big(\frac{\sqrt2}{2},\frac{\sqrt2}{2}\Big)
$$

(down-right direction). Any point on that radius has coordinates $t\mathbf{u}$ and distance $t$ from the center.

3. The square is axis-aligned and symmetric about the vertical bisector, so the top-right vertex has coordinates $\big(\tfrac{s}{2},\;y_{\text{top}}\big)$. Because that vertex lies on the right radius its coordinates satisfy

$$
\frac{s}{2}=t\frac{\sqrt2}{2}.
$$

Thus

$$
t=\frac{s}{\sqrt2}.
$$

4. Substitute $s=2\sqrt2$:

$$
t=\frac{2\sqrt2}{\sqrt2}=2.
$$

So the distance from the center to the top-right square vertex is $\boxed{2\text{ m}}$.

(If you like, you can also compute the sector radius $r$ by using the bottom-right vertex; it comes out $r=2\sqrt5$, but that wasn't required.)

--------------
Correctness:

Completeness:

Clarity:

Educational Value:

Tone/Coherence:
--------------

Q6:
Nice work — you were on the right track, but you forgot to account for the different orders the draws can occur in.

**Correct reasoning (two ways):**

**1) Order approach (what you started):**
The probability of drawing Red, Red, Blue in that *specific* order is

$$
\frac{3}{8}\cdot\frac{2}{7}\cdot\frac{5}{6}=\frac{3\cdot2\cdot5}{8\cdot7\cdot6}=\frac{30}{336}=\frac{5}{56}.
$$

But there are $\binom{3}{2}=3$ possible orders that give exactly 2 reds and 1 blue (R,R,B; R,B,R; B,R,R). So multiply by 3:

$$
3\cdot\frac{5}{56}=\frac{15}{56}.
$$

**2) Hypergeometric (combinatorial) approach:**
Choose 2 reds out of 3 and 1 blue out of 5, divided by choosing any 3 balls out of 8:

$$
\frac{\binom{3}{2}\binom{5}{1}}{\binom{8}{3}}=\frac{3\cdot5}{56}=\frac{15}{56}.
$$

**Final answer:** $\displaystyle \frac{15}{56}$, which is about $0.267857$ (≈ 26.79%).

So your per-order probability calculation was correct, but you must multiply by 3 because any of the three draw orders with exactly two reds and one blue works.

--------------
Correctness:

Completeness:

Clarity:

Educational Value:

Tone/Coherence:
--------------

