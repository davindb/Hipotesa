package com.karyaanakbangsa.tracksymptomsimple.data

data class PredictionResponse(
    val Description: String,
    val Disease: String,
    val Precaution: List<String>,
    val Probability: Double
)
