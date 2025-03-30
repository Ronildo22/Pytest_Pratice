## Pytest execute CLI

Execute pytest verbose. Look PASSED. Deafault pytest look "." when tests passed

```bash
pytest caminho_arquivo -v
```

---

## Coverage Tests

Generate HTML for covarage tests execute code in terminal is below:

```bash
covarage html

```

Execute covarage in tests a determined file

```bash
pytest --cov=caminho_arquivo
```

## Type Tests

---

```python
from dataclasses import dataclass
from datetime import datetime

# ------------------
# Test Scheme


@dataclass
class Tarefa:
    id: int
    nome: str
    data: datetime
# ------------------
```
