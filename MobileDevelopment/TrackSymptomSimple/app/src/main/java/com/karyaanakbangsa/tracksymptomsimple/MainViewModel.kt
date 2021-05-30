package com.karyaanakbangsa.tracksymptomsimple

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.karyaanakbangsa.tracksymptomsimple.data.PredictionResponse
import com.karyaanakbangsa.tracksymptomsimple.data.SymptomsBody
import com.karyaanakbangsa.tracksymptomsimple.repository.Repository
import kotlinx.coroutines.launch

class MainViewModel(private val repository: Repository) : ViewModel() {

    val predictionResponse = MutableLiveData<PredictionResponse>()

    fun pushPost(post: SymptomsBody) {
        viewModelScope.launch {
            val response = repository.postSymptoms(post)
            Log.d("Response", response.body().toString())
            predictionResponse.postValue(response.body())
            Log.d("Response Code", response.code().toString())
        }
    }
    fun getResponse(): LiveData<PredictionResponse>{
        return predictionResponse
    }
}