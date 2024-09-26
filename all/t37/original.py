import numpy as np


def lancz(n, quadrature_rule):
    """Implements the Lanczos algorithm for computing the coefficients of the
    recurrent relations of the orthogonal polynomials.

    This was generated by CoPilot from the Fortran code of Gautschi.
    """
    x = quadrature_rule.x
    w = quadrature_rule.w
    alpha = np.zeros(n)
    beta = np.zeros(n)
    dp0 = np.zeros(len(x))
    dp1 = np.zeros(len(x))
    if n <= 0 or n > len(x):
        raise ValueError('n must be between 1 and len(x).')
    else:
        for i in range(len(x)):
            dp0[i] = x[i]
            dp1[i] = 0.0
        dp1[0] = w[0]
        for i in range(len(x) - 1):
            dpi = w[i + 1]
            dgam = 1.0
            dsig = 0.0
            dt = 0.0
            xlam = x[i + 1]
            for k in range(i + 1):
                drho = dp1[k] + dpi
                dtmp = dgam * drho
                dtsig = dsig
                if drho <= 0.0:
                    dgam = 1.0
                    dsig = 0.0
                else:
                    dgam = dp1[k] / drho
                    dsig = dpi / drho
                dtk = dsig * (dp0[k] - xlam) - dgam * dt
                dp0[k] = dp0[k] - (dtk - dt)
                dt = dtk
                if dsig <= 0.0:
                    dpi = dtsig * dp1[k]
                else:
                    dpi = (dt ** 2) / dsig
                dtsig = dsig
                dp1[k] = dtmp
        for k in range(n):
            alpha[k] = dp0[k]
            beta[k] = dp1[k]

        gamma = np.ones(n)

        return OrthogonalPolynomial(alpha, beta, gamma, quadrature_rule)