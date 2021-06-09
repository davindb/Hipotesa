package com.karyaanakbangsa.tracksymptom.ui

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import com.karyaanakbangsa.tracksymptom.data.Repository
import com.karyaanakbangsa.tracksymptom.data.Symptoms
import com.karyaanakbangsa.tracksymptom.data.SymptomsDatabase

class MainViewModel(application: Application): AndroidViewModel(application) {

    val readAllData: LiveData<List<Symptoms>>
    private val repository: Repository

    init{
        val symptomsDao = SymptomsDatabase.getDatabase(application).symptomsDao()
        repository = Repository(symptomsDao)
        readAllData = repository.readAllData
    }

}