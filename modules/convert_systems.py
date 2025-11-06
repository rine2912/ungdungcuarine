def convert_number(number: str, from_base: int, to_base: int) -> str:
    try:
        if from_base == 10 and '.' in number:
            num = float(number.replace(',', '.'))
            int_part = int(num)
            frac_part = num - int_part
            int_str = format(int_part, {2:'b',8:'o',10:'d',16:'X'}[to_base])
            def frac_to_base(frac, base, prec=8):
                out = ''
                for _ in range(prec):
                    frac *= base
                    d = int(frac)
                    frac -= d
                    out += (str(d) if d < 10 else chr(ord('A')+d-10))
                return out
            frac_str = frac_to_base(frac_part, to_base)
            return f"{int_str}.{frac_str}"
        decimal = int(number, from_base)
        if to_base == 2:
            return bin(decimal)[2:]
        if to_base == 8:
            return oct(decimal)[2:]
        if to_base == 10:
            return str(decimal)
        if to_base == 16:
            return hex(decimal)[2:].upper()
        return str(decimal)
    except Exception:
        return "⚠️ Lỗi chuyển đổi!"
