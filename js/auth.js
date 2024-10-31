import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js";
import { getAuth, createUser, signInUser } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-auth.js";
import { getFirestore, setDoc, doc } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-firestore.js";

const firebaseConfig = {
    apiKey: "AIzaSyCXDY_NCzEXeabDbcj2OMXrbpME58nQvd0",
    authDomain: "farmacia-da5ab.firebaseapp.com",
    projectId: "farmacia-da5ab",
    storageBucket: "farmacia-da5ab.appspot.com",
    messagingSenderId: "1021626167951",
    appId: "1:1021626167951:web:0a19ee3d0f6e007075f6fa",
    measurementId: "G-D4TEEZNF2N"
};

  // Initialize Firebase
const app = initializeApp(firebaseConfig);