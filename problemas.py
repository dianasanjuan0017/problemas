import numpy as np

class ProblemaC18:
    def __init__(self, offset):
        self.tolerance = 1e-4
        self.offset = np.asarray(offset, dtype=float)
        self.D = len(self.offset)
        self.lower_bounds = np.full(self.D, -50.0)
        self.upper_bounds = np.full(self.D,  50.0)

    def get_limites(self):
        return self.lower_bounds, self.upper_bounds

    def evaluate(self, individuo):
        x = np.asarray(individuo, dtype=float)
        z = x - self.offset
        fitness = self.aptitud(z)
        suma_violaciones = self.sumar_violation(z)
        feasible = suma_violaciones <= self.tolerance
        return fitness, suma_violaciones

    def aptitud(self, z):
        diffs = z[:-1] - z[1:]
        return np.sum(diffs**2)

    def g(self, z):
        return (1 / self.D) * np.sum(-z * np.sin(np.sqrt(np.abs(z))))

    def h(self, z):
        return (1 / self.D) * np.sum(z * np.sin(np.sqrt(np.abs(z))))

    def sumar_violation(self, z):
        h_val = self.h(z)
        g_val = self.g(z)
        viol_h = max(0.0, abs(h_val) - self.tolerance)
        viol_g = max(0.0, g_val)
        return viol_h + viol_g

class ProblemaC13:
    def __init__(self, offset):
        self.tolerance = 1e-4
        self.offset = np.asarray(offset, dtype=float)
        self.D = len(self.offset)
        self.lower_bounds = np.full(self.D, -100.0)
        self.upper_bounds = np.full(self.D, 100.0)

    def get_limites(self):
        return self.lower_bounds, self.upper_bounds

    def evaluate(self, individuo):
        x = np.asarray(individuo, dtype=float)
        z = x - self.offset
        fitness = self.aptitud(z)
        suma_violaciones = self.sumar_violation(z)
        feasible = suma_violaciones <= self.tolerance
        return fitness, suma_violaciones

    def aptitud(self, z):
        return np.sum(z**2)

    def g(self, z):
        return np.sum(np.abs(z)) - 1000  # desigualdad: <= 0

    def h(self, z):
        return np.sum(z)  # igualdad: = 0

    def sumar_violation(self, z):
        h_val = self.h(z)
        g_val = self.g(z)
        viol_h = max(0.0, abs(h_val) - self.tolerance)
        viol_g = max(0.0, g_val)
        return viol_h + viol_g

class Problema2020_4:
    def __init__(self, offset):
        self.tolerance = 1e-4
        self.offset = np.asarray(offset, dtype=float)
        self.D = len(self.offset)
        self.lower_bounds = np.full(self.D, -100.0)
        self.upper_bounds = np.full(self.D, 100.0)

    def get_limites(self):
        return self.lower_bounds, self.upper_bounds

    def evaluate(self, individuo):
        x = np.asarray(individuo, dtype=float)
        z = x - self.offset
        fitness = self.aptitud(z)
        suma_violaciones = self.sumar_violation(z)
        feasible = suma_violaciones <= self.tolerance
        return fitness, suma_violaciones

    def aptitud(self, z):
        return np.sum(z**2)

    def g(self, z):
        return np.sum(z[:self.D//2]**2) - 100  # desigualdad

    def h(self, z):
        return np.sum(z[self.D//2:]**2) - 100  # igualdad

    def sumar_violation(self, z):
        h_val = self.h(z)
        g_val = self.g(z)
        viol_h = max(0.0, abs(h_val) - self.tolerance)
        viol_g = max(0.0, g_val)
        return viol_h + viol_g

class Problema2021_6:
    def __init__(self, offset):
        self.tolerance = 1e-4
        self.offset = np.asarray(offset, dtype=float)
        self.D = len(self.offset)
        self.lower_bounds = np.full(self.D, -100.0)
        self.upper_bounds = np.full(self.D, 100.0)

    def get_limites(self):
        return self.lower_bounds, self.upper_bounds

    def evaluate(self, individuo):
        x = np.asarray(individuo, dtype=float)
        z = x - self.offset
        fitness = self.aptitud(z)
        suma_violaciones = self.sumar_violation(z)
        feasible = suma_violaciones <= self.tolerance
        return fitness, suma_violaciones

    def aptitud(self, z):
        return np.sum(np.square(np.cumsum(z)))

    def g(self, z):
        return np.max(np.abs(z)) - 50  # desigualdad

    def h(self, z):
        return np.mean(z)  # igualdad: promedio debe ser 0

    def sumar_violation(self, z):
        h_val = self.h(z)
        g_val = self.g(z)
        viol_h = max(0.0, abs(h_val) - self.tolerance)
        viol_g = max(0.0, g_val)
        return viol_h + viol_g
