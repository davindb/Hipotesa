package com.karyaanakbangsa.tracksymptom.data

data class SymptomsResponse(
    val Description: String,
    val Disease: String,
    val Precaution: List<String>,
    val Probability: Double
)