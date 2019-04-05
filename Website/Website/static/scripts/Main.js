function HelloJS() {
    console.log("Hello");
    alert("Hello again");
}

function formsubmit(formData) {
    console.log("Test");

    // Declaring a new function called 'sendformdata' which takes 1 arguement which is 'formdata'
    function sendFormData(formData) {
        //Declaring an object called request which has the value XMLHttpRequest
        const request = new XMLHttpRequest();
        //Declaring an object called FD which has the value FormData
        const FD = new FormData();
        console.log(formData);
        console.log(FD);

        //A for loop which will create a variable called 'name' which will increment by 1 until the value equals the values in formData
        for (name in formData) {
            //add the name to the object FD from formData -(transfers everything from formData to FD)
            FD.append(name, formData[name]);
        }

        //Will open a request to travel to the 'create' directory - 'POST' tells us that it will send data there
        request.open("POST", "../create");

        //An event listener is created here which will wait until the post is loaded and ready to be sent
        request.addEventListener("load", () => {
            //tells the user in the form of a popup when the post is ready to be sent
            alert("Data has been sent!");

        });

       
        //Waiting for the state change
        request.onreadystatechange((xhr) => {
            // This is checking for ready state 4 and a 200 response (HTML code for OK)
            if (xhr.readyState === 4 && xhr.status == 200) {
                //If readystate equals 4 and the html code is 200, tell the user that the post has been added successfully
                alert("Post Added successfully");
            }
        });

        //Sends the request
        request.send();
    }

    //Calls the function sendFormData and passes formData to the function.
    sendFormData(formData);


}

function initevents() {
    const button = document.getElementById("submitbutton");

    button.addEventListener("click", function () {
        const title = document.getElementById("titleform").textContent;
        const date = document.getElementById("dateform").textContent;
        const content = document.getElementById("contentform").textContent;
        const payload = {};
        payload[title] = { date: date, content: content }

        const request = new XMLHttpRequest();

        request.open("POST", "/dailyposts/create");

        request.addEventListener("load", () => {
            alert("Data has been sent!");
        });

        request.onreadystatechange = (xhr) => {
            if (xhr.readyState === 4 && xhr.status == 200) {
                alert("Post Added successfully");
            }
        };

        request.send(JSON.stringify(payload));


    });

}

initevents();