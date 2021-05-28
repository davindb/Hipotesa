package com.karyaanakbangsa.tracksymptom.data

import androidx.lifecycle.LiveData
import androidx.room.Room

class Repository(private val symptomsDao: SymptomsDao) {

    val readAllData: LiveData<List<Symptoms>> = symptomsDao.readAllData()

}