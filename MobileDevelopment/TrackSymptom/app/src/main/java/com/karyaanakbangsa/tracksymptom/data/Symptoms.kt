package com.karyaanakbangsa.tracksymptom.data

import androidx.annotation.NonNull
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "symptoms_table")
data class Symptoms(
    @PrimaryKey(autoGenerate = true)
    var id: Int = 0,
    @NonNull
    var symptomsName: String )