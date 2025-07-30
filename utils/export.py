import pandas as pd
import io

def export_to_excel(data):
    df = pd.DataFrame([data])
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    return output
