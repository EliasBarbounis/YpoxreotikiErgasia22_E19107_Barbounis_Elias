# DigitalNotes

<ol>
  <li>Download the files</li>
  <li>Open a Terminal in the directory of the project</li>
  <li>Type sudo docker-compose up</li>
  <li>Open a web browser and in the url put “http://127.0.0.1:5000”</li>
</ol>
  <h4>Mongodb Data</h4>
<ul>
  <li><h5>Single Users:{'email': email, 'username': username, 'fullname': fullname, 'password': password, 'type': "simple_user"}</h5></li>
  <li><h5>Admin Users:{'email': email, 'username': username, 'password': password, 'type': "admin_user"}</h5></li>
  <li><h5>Notes:{username': username, 'title': title, 'noteText': noteText, 'keywords': keywords, 'date': date}</h5></li>
  </ul>
<h3> Functions</h3>
<ul>
  <li>
     <h3>Home page</h3>
      <h5>Sign up,Log in</h5>
      <img src='Screenshots/Screenshot from 2022-07-06 00-44-52.png'></img> 
      <h4>Sign up</h4>
      <h5>User inserts the fields to Sign up.</h5>
      <img src='Screenshots/Screenshot from 2022-07-06 00-47-03.png'></img>
      <h4>User Sign up (When there is already a user with this e-mail)</h4>
      <img src='Screenshots/Screenshot from 2022-07-06 00-47-43.png'></img>
      <h4>User Sign up (When there is already a user with this username)</h4>
      <img src='Screenshots/Screenshot from 2022-07-06 00-48-34.png'></img>    
      <h4>User/Admin Log in.</h4>
      <img src='Screenshots/Screenshot from 2022-07-06 00-49-49.png'></img> 
      <h4>User/Admin Log in (In case of wrong password).</h4>
      <img src='Screenshots/Screenshot from 2022-07-06 00-50-20.png'></img> 
      <h4>User/Admin Log in (In case of wrong credentials).</h4>
      <img src='Screenshots/Screenshot from 2022-07-06 00-50-55.png'></img> 
    </li>
    <li>
      <h3>User Home page</h3>
      <h4>Functions: Movie search,Book tickets</h4>
      <img src='Screenshots/user_page.png'></img>
      <h4>Movie search</h4>
      <h5>User types in the movie title they wish to book tickets for.</h5>
      <img src='Screenshots/user_search2.png'></img>
      <h4>Ticket Book</h4>
      <h5>User types in amount of tickets they wish to book.
      <img src='Screenshots/user_book_sits.png'></img>
      <h4>Submit Order</h4>
      <img src='Screenshots/user_submit_order.png'></img>
      <h4>Book Succesful</h4>
      <img src='Screenshots/user_book_succesful.png'></img>
      <h4>User History</h4>
      <h5>User can see what movies they have booked tickets for.</h5>
      <img src='Screenshots/user_history.png'></img>
    </li>
    <li>
      <h3>Admin Home page</h3>
      <h4>Functions: Insert,Update,Delete Movie & Add new Admin User</h4>
      <img src='Screenshots/admin_page.png'></img>
      <h4>Insert Movie</h4>
      <h5>Admin types in Title,Release Date,Description and Screening Dates for the Movie they wish to insert to the database.</h5>
      <img src='Screenshots/admin_insert_movie.png'></img>
      <img src='Screenshots/admin_insert_movie2.png'></img>
      <h4>Update Movie</h4>   
      <h5>Admin finds and updates Movies info.</h5>
      <img src='Screenshots/admin_movie_update2.png'></img>
      <img src='Screenshots/admin_movie_update3.png'></img>
      <img src='Screenshots/admin_movie_update_success.png'></img>
      <h4>Delete Movie</h4>   
      <h5>Admin finds and deletes Movie form database.</h5>
      <img src='Screenshots/admin_movie_delete.png'></img>
      <h4>Delete Movie (Fail)</h4>
      <img src='Screenshots/admin_movie_delete_fail.png'></img>
      <h4>Add new Admin</h4>
      <h5>Admin adds credentials of new system admin.</h5>
      <img src='Screenshots/admin_new_admin.png'></img>
      <img src='Screenshots/admin_new_admin2.png'></img>
      <h4>Add new Admin (Fail)</h4>
      <img src='Screenshots/admin_new_admin_fail.png'></img>
    </li>
</ul>
