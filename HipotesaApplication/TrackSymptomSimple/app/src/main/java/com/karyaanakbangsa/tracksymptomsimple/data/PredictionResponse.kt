package com.karyaanakbangsa.tracksymptomsimple.data

data class PredictionResponse(
    val Description: String,
    val Disease: String,
    val Precaution: ArrayList<String>,
    val Probability: Double
)
