## load_data.sh


```bash
#!/bin/bash
set -e


# Usage: ./load_data.sh


python manage.py loaddata shop/fixtures/products.json
```


Make executable: chmod +x load_data.sh


---
