from datetime import datetime, timezone
import re
from typing import List, Tuple


def now_iso() -> str:
    """Return timezone-aware ISO timestamp."""
    return datetime.now(timezone.utc).isoformat()


def plate_valid(reg: str) -> bool:
    """Sodda avtomobil raqami validatsiyasi (helper).

    Keep same logic as previous implementation but extracted.
    """
    if not isinstance(reg, str):
        return False
    reg = reg.strip()
    if any(c.islower() for c in reg):
        return False
    pattern = r"^[0-9]{2}[A-Z][0-9]{3}[A-Z]{2}$"
    if re.fullmatch(pattern, reg):
        return True
    if 2 <= len(reg) <= 9 and re.search(r"[0-9]", reg) and re.search(r"[A-Z]", reg):
        return True
    return False


def format_parking_table(slots: List, cars: List[dict], reservations: List[dict]) -> str:
    """Format parking slots, cars and reservations into a table string.

    This is a pure helper so `Parking` methods remain small.
    """
    rows: List[Tuple[str, str, str, str, str]] = []
    for i, s in enumerate(slots):
        reserved = next((r for r in reservations if r.get("slot") == i), None)
        if s is None and not reserved:
            rows.append((str(i), "No", "", "", ""))
        elif reserved and s is None:
            rows.append((str(i), "Reserved", "", reserved.get("owner"), reserved.get("time")[:19]))
        else:
            car = next((c for c in cars if c.get("reg_number") == s), None)
            reg = s
            owner = car.get("owner") if car else ""
            entry = (car.get("entry_time")[:19] if car and car.get("entry_time") else "")
            rows.append((str(i), "Yes", reg, owner, entry))

    headers = ("Slot", "Occupied", "Reg", "Owner", "Entry Time")
    cols = list(zip(*([headers] + rows))) if rows else [headers]
    widths = [max(len(str(x)) for x in col) for col in cols]
    sep = " | "
    header_line = sep.join(h.ljust(widths[idx]) for idx, h in enumerate(headers))
    divider = "-+-".join("-" * w for w in widths)
    lines = [header_line, divider]
    for r in rows:
        lines.append(sep.join(str(r[col]).ljust(widths[col]) for col in range(len(r))))
    return "\n".join(lines)
