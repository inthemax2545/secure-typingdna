import { TypingDNA } from "./typingdna.js";

const tdna = new TypingDNA();

const loginButtton = document.getElementById("login-button");
if (loginButtton) {
    loginButtton.addEventListener("click", () => loginOrSignup(true));
    tdna.addTarget("email");
    tdna.addTarget("password");
}

const signUpButtton = document.getElementById("sign-up-button");
if (signUpButtton) {
    signUpButtton.addEventListener("click", () => loginOrSignup(false));
    tdna.addTarget("email");
    tdna.addTarget("password");
}

const typingPatternsButtton = document.getElementById("styping-patterns-button");
if (typingPatternsButtton) {
    typingPatternsButtton.addEventListener("click", () => loginOrSignup(false));
    tdna.addTarget("email");
    tdna.addTarget("password");
}

export function loginOrSignup(login=true) {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    let endpoint;
    if (login) {
        endpoint = "/api/login";
    }
    else {
        endpoint = "/api/sign-up";
    }

    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({email: email, password: password}),
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.user_id) {
            sendTypingData(data.user_id, email + password);
        }
        else if (data.message) {
            alert(data.message);
        }
    });
}

function sendTypingData(id, text) {
    const pattern = tdna.getTypingPattern({
        type: 1,
        text: text,
    });
        fetch("/typingdna", {
            method: "POST",
            headers: { 
                "Content-Type": "application/json",
            },
            body: JSON.stringify({pattern: pattern, user_id: id}),
    })
        .then((res) => res.json())
        .then((data) => console.log(data));
}