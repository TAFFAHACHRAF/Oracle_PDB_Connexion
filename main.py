import cx_Oracle
from fastapi import FastAPI

app = FastAPI()

dsn = cx_Oracle.makedsn(
    host='localhost',
    port=1521,
    sid='ORCLCDB'
)

pdb = 'PATIENTMANAGEMENT'
username = 'sysdba'
password = 'azoiazidOIJyNewPassword123'

dsn_str = cx_Oracle.makedsn(
    host='localhost',
    port=1521,
    service_name=f'{pdb}'
)

@app.on_event("startup")
def startup_event():
    global connection
    connection = cx_Oracle.connect(
        user=username,
        password=password,
        dsn=dsn_str,
        encoding="UTF-8",
        nencoding="UTF-8",
        mode=cx_Oracle.SYSDBA # ou cx_Oracle.SYSOPER selon votre besoin
    )

    
@app.on_event("shutdown")
def shutdown_event():
    connection.close()

@app.get("/")
async def root():
    with connection.cursor() as cursor:
        cursor.execute("SELECT 'Hello, world!' FROM DUAL")
        result = cursor.fetchone()[0]
    return {"message": result}
