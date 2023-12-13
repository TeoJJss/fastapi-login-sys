<h1>Basic Login System</h1>
<p>This is a basic login system that will create ticket upon successful user login. The backend server is built using FastAPI. </p>
<h2>Getting Started</h2>
<h3>Prerequisite</h3>
<b>Python v3.11.6</b> is used for development. 
<h3>Installing</h3>
<p>Run the following commands to create a virtual environment and install all necessary dependencies:</p>

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
<p>Then, run the following command to launch the backend server</p>

```
uvicorn app:app
```  
You will notice that a ".db" file is created. That is a SQLite database used to store data!  
To launch frontend, double click `index.html` to open it in browser.  

<h2>User Guide</h2>

`index.html` is the initial landing page for login, and `home.html` is only accessible upon successful login.  
Please open the HTML files directly in browser, after launching the backend server.  
The table below shows the existing user credentials for login: 
<table>
    <thead>
        <tr>
            <th>Username</th>
            <th>Password</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John Doe</td>
            <td>john123</td>
        </tr>
        <tr>
            <td>Oyen</td>
            <td>cuteOyen</td>
        </tr>
    </tbody>
</table>
<i>All the credentials are case-sensitive</i><br>

After entering username and password accordingly, click "Login" button to login. Upon successful login, user will be redirected to `home.html`.  
In `home.html`, user can click "Logout" hyperlink to log out. After logging out, the user cannot access `home.html`. 

<h2>Developer Guide</h2>
Before launching the backend server, developers should take note the following tips:<br>

1. To change the ".db" filename, do it at `config.py`. 
2. If you launch the backend server in different port number (other than 8000), please modify the host and port number at `src/functions.js`.
3. If you would like to add more authenticated users, please modify the SQL in the `insert_users_sql` variable at `services/service.py`. 

All authenticated users are stored in the `USERS` table. Upon successful login, the backend system will create a ticket and add both username and ticket string to the `TICKETS` table. The ticket will be saved in session variable of the browser too.  
When `home.html` is accessed, the system will retrieve the ticket string in the session variable and check if its existence in `TICKETS` table.  
When user logout, the system delete the ticket string from the `TICKETS` table. The session variable is removed from the frontend side. This will restrict the user to access the `home.html` or other authenticated webpages.     
Frontend and backend are integrated through FastAPI.   