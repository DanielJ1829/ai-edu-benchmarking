Q1:
Short answer: your teacher is right — the antiderivative you wrote is incorrect. The correct general antiderivative is

$$
F(x)=\frac{e^x}{2}\big(\sin x-\cos x\big)+C,
$$

and the definite integral from $\theta_1=\tfrac{3\pi}{4}$ to $\theta_2=\tfrac{\pi}{6}$ equals

$$
\int_{3\pi/4}^{\pi/6} e^x\sin x\,dx
= \frac{e^{\pi/6}}{4}(1-\sqrt3)\;-\;\frac{e^{3\pi/4}}{2}\sqrt2
\approx -7.76943078.
$$

Why your antiderivative is wrong (where the sign/factor error comes from)

Start with $I=\int e^x\sin x\,dx$. Integration by parts once (take $u=\sin x,\;dv=e^x dx$) gives

$$
I=e^x\sin x-\int e^x\cos x\,dx.
$$

Integrate the remaining integral by parts again (now $u=\cos x,\;dv=e^x dx$):

$$
\int e^x\cos x\,dx = e^x\cos x - \int e^x(-\sin x)\,dx
= e^x\cos x + \int e^x\sin x\,dx
= e^x\cos x + I.
$$

Substitute that back:

$$
I = e^x\sin x - (e^x\cos x + I) = e^x\sin x - e^x\cos x - I.
$$

So $2I = e^x(\sin x-\cos x)$, hence

$$
I=\frac{e^x}{2}(\sin x-\cos x)+C,
$$

as claimed.

Your answer $F(x)=e^x(\sin x+\cos x)+C$ would give $F'(x)=e^x(2\cos x)$, not $e^x\sin x$; so that is the algebra/sign mistake.

Definite integral (numeric)

$$
F\!\left(\tfrac{\pi}{6}\right)=\frac{e^{\pi/6}}{2}\Big(\tfrac12-\tfrac{\sqrt3}{2}\Big)=\frac{e^{\pi/6}(1-\sqrt3)}{4},
\qquad
F\!\left(\tfrac{3\pi}{4}\right)=\frac{e^{3\pi/4}}{2}\cdot\sqrt2.
$$

So

$$
\int_{3\pi/4}^{\pi/6} e^x\sin x\,dx
=F(\tfrac{\pi}{6})-F(\tfrac{3\pi}{4})
=\frac{e^{\pi/6}(1-\sqrt3)}{4}-\frac{e^{3\pi/4}\sqrt2}{2}
\approx -7.76943.
$$

You're doing the right kind of method (IBP twice) — just be careful with the minus signs when substituting and when bringing the integral to the left-hand side. Nice work attempting it; this is a common place to slip. If you want, I can show a one-line verification (differentiate the correct $F(x)$) or help you trace exactly which step in your original working produced the wrong sign.

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q2:
Nice work spotting the standard-looking form — but you’re missing one factor of $v_0$. Your expression has the wrong units (it gives seconds, not metres), which is a quick red flag.

Here’s a short derivation and the correct result.

Take horizontal $x$ and vertical $y$ (up positive). Launch from the origin with

$$
v_x=v_0\cos\theta,\qquad v_y=v_0\sin\theta,
$$

so

$$
x(t)=v_0\cos\theta\,t,\qquad y(t)=v_0\sin\theta\,t-\tfrac12 g t^2.
$$

The slope (going down at angle $\alpha$) has equation $y=-x\tan\alpha$. Impact when

$$
v_0\sin\theta\,t-\tfrac12 g t^2=-v_0\cos\theta\,t\tan\alpha.
$$

For $t>0$ this gives

$$
t=\frac{2v_0\big(\sin\theta+\cos\theta\tan\alpha\big)}{g}
=\frac{2v_0\sin(\theta+\alpha)}{g\cos\alpha}.
$$

Horizontal distance at impact is $x=v_0\cos\theta\,t$. The distance along the slope $R$ relates to the horizontal distance by $x=R\cos\alpha$, so

$$
R=\frac{x}{\cos\alpha}=\frac{v_0\cos\theta\,t}{\cos\alpha}
=\frac{2v_0^2\cos\theta\sin(\theta+\alpha)}{g\cos^2\alpha}.
$$

So the correct formula has $v_0^2$ in the numerator (not $v_0$). Plugging in your numbers ($\alpha=15^\circ,\ v_0=20\ \mathrm{m/s},\ \theta=30^\circ,\ g=9.81\ \mathrm{m/s^2}$):

$$
R\approx 53.52\ \text{m}.
$$

Your value $2.68\ \mathrm{m}$ comes from the same algebra but with the extra factor of $v_0$ accidentally dropped — that’s why it’s three orders of magnitude too small and has wrong units. So your teacher was right to mark it incorrect (unless the problem had some different geometry or a different reference height). If you want, I can show the algebra symbol-by-symbol or make a small diagram to visualise the geometry.

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q3:
Nice work spotting the equation and trying the quadratic formula — you were almost there. The mistake is a sign error when you substituted the constant term.

Step-by-step:

Original:

$$
3x^2+(p+3k)x-(p^2-3k)=0.
$$

Put $p=2,\;k=1$:

$$
p+3k=2+3(1)=5,\qquad -(p^2-3k)=-(2^2-3\cdot1)=-(4-3)= -1.
$$

So the quadratic is

$$
3x^2+5x-1=0,
$$

where $a=3,\;b=5,\;c=-1$. (The crucial point: $c=-1$, not $+1$.)

Discriminant:

$$
\Delta=b^2-4ac=5^2-4\cdot3\cdot(-1)=25+12=37.
$$

Roots (quadratic formula):

$$
x=\frac{-5\pm\sqrt{37}}{6}.
$$

Numeric approximations:

$$
x_1\approx\frac{-5+\sqrt{37}}{6}\approx0.18046,\qquad
x_2\approx\frac{-5-\sqrt{37}}{6}\approx-1.84713.
$$

Root behavior for $k=1,p=2$:

* The discriminant $37>0$ so the equation has two distinct real roots.
* One root is positive ($\approx0.1805$) and the other is negative ($\approx-1.8471$).
* By Vieta: sum of roots $= -\frac{b}{a}=-\frac{5}{3}\approx-1.6667$, product $=\frac{c}{a}=-\frac{1}{3}\approx-0.3333$ — consistent with the numerical roots.

So your method was right, but you used $c=+1$ when computing the discriminant (that produced $\sqrt{13}$). The correct discriminant is $37$, so the correct roots are $\displaystyle\frac{-5\pm\sqrt{37}}{6}$.


------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q4:
Nice work setting it up — you were close, but there’s a simple arithmetic/inversion slip. Walk-through:

Resistors $R_1$ and $R_2$ in parallel give equivalent resistance

$$
R_{12}=\frac{R_1R_2}{R_1+R_2}=\frac{10\cdot20}{10+20}=\frac{200}{30}=\frac{20}{3}\ \Omega\approx6.67\ \Omega.
$$

Current through those two (total $I_1+I_2$) with $V=12\ \text{V}$ is

$$
I_1+I_2=\frac{V}{R_{12}}=\frac{12}{20/3}=12\cdot\frac{3}{20}=\frac{36}{20}=1.8\ \text{A}.
$$

(Your step $12/(3/20)=80$ inverted the fraction — $20/3$ is about $6.67$, not $3/20$.)

So $I_3$ must equal $1.8\ \text{A}$. Then

$$
R_3=\frac{V}{I_3}=\frac{12}{1.8}=\frac{120}{18}=\frac{20}{3}\ \Omega\approx6.67\ \Omega.
$$

You can also check by individual currents:

$$
I_1=\frac{12}{10}=1.2\ \text{A},\qquad I_2=\frac{12}{20}=0.6\ \text{A},\qquad I_1+I_2=1.8\ \text{A},
$$

so $I_3=1.8$ gives the same result.

Conclusion: the correct $R_3$ is $20/3\ \Omega$ (≈6.67 Ω). Your method was right in spirit; the error was a small arithmetic/inversion mistake that produced the absurd 80 A.

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q5:
Nice work thinking it through — you were close, but your step $x=\tfrac r2$ is the mistake. The square doesn't put that point at half the radius. Here's a clean way to see it and get the correct area.

Place the quarter-circle of radius $r$ in the first quadrant with center at the origin and radii along the $x$- and $y$-axes. Let the top two vertices of the square be

$$
(0,t)\quad\text{and}\quad(t,0),
$$

so the top side of the square has length $a=\sqrt{(t-0)^2+(0-t)^2}=t\sqrt2$. The square extends perpendicularly downwards from that top side; the bottom two vertices (which lie on the arc) are then

$$
(2t,t)\quad\text{and}\quad(t,2t),
$$

because the perpendicular displacement equals $a/\sqrt2=t$.

Those bottom vertices lie on the circle $x^2+y^2=r^2$. Use $(2t,t)$:

$$
(2t)^2+t^2= r^2 \quad\Rightarrow\quad 5t^2=r^2 \quad\Rightarrow\quad t=\frac{r}{\sqrt5}.
$$

Thus the square side length is

$$
a=t\sqrt2=r\sqrt{\tfrac{2}{5}},
$$

and its area is

$$
A=a^2=r^2\cdot\frac{2}{5}.
$$

With $r=10$ this gives

$$
A=100\cdot\frac{2}{5}=40\ \text{m}^2.
$$

So the correct area is $40\ \text{m}^2$. Your assumption $x=r/2$ made the configuration different from the actual geometry of the inscribed square. Nice effort — your approach had the right idea (use symmetry and 45° directions); just one geometric relation was off.

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------
Q6:
You’re close in method (using sequences) but your arithmetic setup missed the black balls — so your teacher is right to mark it wrong.

### Quick correct answer

Use the hypergeometric formula (simplest):

$$
P(\text{exactly }q\text{ reds})=\frac{\binom{m}{q}\binom{n+k}{\,r-q\,}}{\binom{n+m+k}{r}}.
$$

With $(n,m,k,r,q)=(7,5,4,4,3)$:

$$
P=\frac{\binom{5}{3}\binom{11}{1}}{\binom{16}{4}}
=\frac{10\cdot 11}{1820}=\frac{110}{1820}=\frac{11}{182}\approx 0.06044.
$$

So the correct probability is $\boxed{11/182}$, not $14/99$.

### Where your calculation went wrong

You computed (essentially) the probability of “3 reds and 1 blue” while **ignoring the 4 black balls**. Concretely you used denominators 12, 11, 10, 9 (red+blue = 12) instead of the full population 16, 15, 14, 13. Also the non-red draw could be **blue or black**; you only counted blue (7 left) and excluded the 4 blacks.

### Check by the sequential (order) method

Pick a particular order e.g. R,R,R,non-red:

$$
\Pr(R,R,R,\text{non-red})=\frac{5}{16}\cdot\frac{4}{15}\cdot\frac{3}{14}\cdot\frac{11}{13}.
$$

There are 4 possible positions for the non-red, so multiply by 4:

$$
4\cdot\frac{5\cdot4\cdot3\cdot11}{16\cdot15\cdot14\cdot13}
=\frac{2640}{43680}=\frac{11}{182},
$$

which agrees with the hypergeometric result.

If you want, I can show a short explanation of the hypergeometric formula or walk through more sequence examples.

------------

Correctness:
Completeness:
Clarity:
Educational Value:
Tone/Coherence:

-----------