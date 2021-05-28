package com.karyaanakbangsa.tracksymptom.data

import androidx.lifecycle.LiveData
import androidx.room.Dao
import androidx.room.Query

@Dao
interface SymptomsDao {

    @Query("SELECT * FROM symptoms_table ORDER BY id ASC")
    fun readAllData(): LiveData<List<Symptoms>>
}