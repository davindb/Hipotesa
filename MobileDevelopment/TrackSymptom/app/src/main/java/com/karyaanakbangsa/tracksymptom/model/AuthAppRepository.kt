package com.karyaanakbangsa.tracksymptom.model

import android.app.Application
import android.os.Build
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.lifecycle.MutableLiveData
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.FirebaseUser

@RequiresApi(Build.VERSION_CODES.P)
class AuthAppRepository {
    private var application: Application? = null

    private var firebaseAuth: FirebaseAuth? = null
    private var userLiveData: MutableLiveData<FirebaseUser?>? = null
    private var loggedOutLiveData: MutableLiveData<Boolean>? = null

    fun AuthAppRepository(application: Application?) {
        this.application = application
        firebaseAuth = FirebaseAuth.getInstance()
        userLiveData = MutableLiveData()
        loggedOutLiveData = MutableLiveData()
        if (firebaseAuth!!.currentUser != null) {
            userLiveData!!.postValue(firebaseAuth!!.currentUser)
            loggedOutLiveData!!.postValue(false)
        }
    }

    fun login(email: String?, password: String?) {
        firebaseAuth!!.signInWithEmailAndPassword(email!!, password!!)
            .addOnCompleteListener(application!!.mainExecutor,
                { task ->
                    if (task.isSuccessful) {
                        userLiveData!!.postValue(firebaseAuth!!.currentUser)
                    } else {
                        Toast.makeText(
                            application!!.applicationContext,
                            "Login Failure: " + task.exception!!.message,
                            Toast.LENGTH_SHORT
                        ).show()
                    }
                })
    }

    fun register(email: String?, password: String?) {
        firebaseAuth!!.createUserWithEmailAndPassword(email!!, password!!)
            .addOnCompleteListener(application!!.mainExecutor,
                { task ->
                    if (task.isSuccessful) {
                        userLiveData!!.postValue(firebaseAuth!!.currentUser)
                    } else {
                        Toast.makeText(
                            application!!.applicationContext,
                            "Registration Failure: " + task.exception!!.message,
                            Toast.LENGTH_SHORT
                        ).show()
                    }
                })
    }

    fun logOut() {
        firebaseAuth!!.signOut()
        loggedOutLiveData!!.postValue(true)
    }

    fun getUserLiveData(): MutableLiveData<FirebaseUser?>? {
        return userLiveData
    }

    fun getLoggedOutLiveData(): MutableLiveData<Boolean>? {
        return loggedOutLiveData
    }
}