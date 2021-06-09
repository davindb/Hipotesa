package com.karyaanakbangsa.tracksymptom.api

import com.karyaanakbangsa.tracksymptom.data.SymptomsPost
import com.karyaanakbangsa.tracksymptom.data.SymptomsResponse
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

interface AiAPi {

    @POST("predict")
    suspend fun postSymptoms(@Body req: SymptomsPost): Call<SymptomsResponse>
}