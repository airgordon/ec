class matrix:
    def __init__(self, rows, field):
        self.rows = rows
        self.field = field
        elems = None
        for row in rows:
            if (elems == None):
                elems = len(row)
            else:
                if elems != len(row):
                    raise Exception("Unequal rows")

    def __mul__(self, other):
        if isinstance(other, list):
            acc = []
            columns = len(self.rows[0])
            if columns < len(other):
                raise Exception()
            m = min(columns, len(other))
            for row in self.rows:
                rowAcc = self.field.zero
                for i in range(0, m):
                    rowAcc = rowAcc + row[i] * other[i]
                acc.append(rowAcc)
            return acc
        else:
            r1 = len(self.rows)
            c1 = len(self.rows[0])
            r2 = len(other.rows)
            c2 = len(other.rows[0])
            if c1 != r2:
                raise Exception("Incomparable size")

            rows = []
            for i in range(0, r1):
                row = []
                for j in range(0, c2):
                    acc = self.field.zero
                    for k in range(0, c1):
                        acc = acc + self.rows[i][k] * other.rows[k][j]
                    row.append(acc)
                rows.append(row)
            return matrix(rows, self.field)

    def _copy(self):
        return [row.copy() for row in self.rows]

    def solve(self, f):

        R = len(self.rows)
        C = len(self.rows[0])

        if R != len(f):
            raise Exception()

        M = self._copy()

        for i in range(0, R):
            M[i].append(f[i])

        C = C + 1
        i = 0  # количество ненулевых строк, количество обработанных строк

        leadColumns = []

        for c in range(0, C - 1):  ## ??????? for c in range(0, R):

            nonZeroRowIdx = None
            nonZeroColumnIdx = None
            for j in range(i, R):
                if M[j][c]:
                    nonZeroRowIdx = j
                    nonZeroColumnIdx = c  ## было nonZeroColumnIdx = j
                    break

            if nonZeroColumnIdx == None:
                continue

            leadColumns.append(nonZeroColumnIdx)

            # если в i-той строке на диагонале ноль - меняем её с другой
            if i != nonZeroRowIdx:  # swap
                zeroRow = M[i]
                nZeroRow = M[nonZeroRowIdx]
                M[i] = nZeroRow
                M[nonZeroRowIdx] = zeroRow

            # нормируем диагональный элемент на единицу
            if M[i][c] != self.field.one:
                h = ~M[i][c]
                for j in range(c, C):
                    M[i][j] = h * M[i][j]

            # обнуляем столбец во всех строках, под этой
            for j in range(i + 1, R):
                if M[j][i]:
                    g = M[j][i]

                    for k in range(0, C):
                        M[j][k] = M[j][k] - M[i][k] * g
            i += 1

        for i in range(len(leadColumns), R):
            if M[i][C - 1]:
                raise Exception("System is not solvable")

        for i in range(len(leadColumns) - 1, 0, -1):
            c = leadColumns[i]
            for j in range(0, i):
                g = M[j][c]
                # M[j][i] = self.field.zero
                for k in range(c, C):  # for k in range(i + 1, n):
                    M[j][k] = M[j][k] - M[i][k] * g

        res = [self.field.zero] * (C - 1)
        for i in range(0, len(leadColumns)):
            res[leadColumns[i]] = M[i][C - 1]

        return res

    def __invert__(self):
        if len(self.rows[0]) != len(self.rows):
            raise Exception("matrix is not square")
        n = len(self.rows)
        inv = []
        for i in range(0, n):
            row = []
            for j in range(0, n):
                if i == j:
                    row.append(self.field.one)
                else:
                    row.append(self.field.zero)
            inv.append(row)

        M = self._copy()
        # inv = self._copy()
        for i in range(0, n):
            nonZeroIdx = None
            for j in range(i, n):
                if M[j][i]:
                    nonZeroIdx = j
                    break

            if nonZeroIdx == None:
                raise Exception()

            # если в i-той строке на диагонале ноль - меняем её с другой
            if i != nonZeroIdx:  # swap
                zeroRow = M[i]
                nZeroRow = M[nonZeroIdx]
                M[i] = nZeroRow
                M[nonZeroIdx] = zeroRow

                zeroRow = inv[i]
                nZeroRow = inv[nonZeroIdx]
                inv[i] = nZeroRow
                inv[nonZeroIdx] = zeroRow

            # нормируем диагональный элемент на единицу
            if M[i][i] != self.field.one:
                h = ~M[i][i]
                M[i][i] = self.field.one
                for j in range(i + 1, n):
                    M[i][j] = h * M[i][j]

                for j in range(0, n):
                    inv[i][j] = h * inv[i][j]

            # обнуляем столбец во всех строках, кроме данной
            for j in range(0, n):
                if j != i and M[j][i]:
                    g = M[j][i]
                    # M[j][i] = self.field.zero
                    for k in range(0, n):  # for k in range(i + 1, n):
                        M[j][k] = M[j][k] - M[i][k] * g
                    for k in range(0, n):
                        inv[j][k] = inv[j][k] - inv[i][k] * g

        return matrix(inv, self.field)
