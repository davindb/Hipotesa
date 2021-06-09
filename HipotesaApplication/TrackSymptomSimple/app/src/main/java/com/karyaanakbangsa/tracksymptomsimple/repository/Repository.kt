package com.karyaanakbangsa.tracksymptomsimple.repository

import com.karyaanakbangsa.tracksymptomsimple.api.RetrofitClient
import com.karyaanakbangsa.tracksymptomsimple.data.PredictionResponse
import com.karyaanakbangsa.tracksymptomsimple.data.SymptomsBody
import retrofit2.Response

class Repository {

    suspend fun postSymptoms(post: SymptomsBody): Response<PredictionResponse> {
        return RetrofitClient.apiService.postSymptoms(post)
    }
}