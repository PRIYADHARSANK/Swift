
import json

with open('payload.json', 'r') as f:
    files = json.load(f)

batch_size = 5
for i in range(0, len(files), batch_size):
    batch = files[i:i + batch_size]
    with open(f'batch_{i//batch_size}.json', 'w') as f_out:
        json.dump(batch, f_out, indent=2)
    print(f'Created batch_{i//batch_size}.json with {len(batch)} files')
