import pyodbc

def connectToDb():
    # Returns a connection to the sql databse specified in the connection string below
    # Note: address of the db can be found in C:\Data\Rio Transformer Tx.x.x.xx\DLL_Data\Quantel\QCIFSBin\Web.config on the transformers
    connection = pyodbc.connect('Driver={SQL Server}; Server=10.162.64.249; Database=orcl; uid=NEWBURY50TEST_12C; pwd=NEWBURY50TEST_12C')
    print 'db_utils.py: Connecting to Momentum Database'
    return connection
  
def closeConnection(connection, cur):
    # Closes the specified connection 
    cur.close()
    del cur
    connection.close()

    
