package com.karyaanakbangsa.tracksymptomsimple.api

import com.karyaanakbangsa.tracksymptomsimple.data.PredictionResponse
import com.karyaanakbangsa.tracksymptomsimple.data.SymptomsBody
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.Headers
import retrofit2.http.POST

interface ApiService {

    @POST("predict")
    @Headers("Content-Type: application/json")
    suspend fun postSymptoms(@Body post: SymptomsBody): Response<PredictionResponse>
}