package com.karyaanakbangsa.tracksymptomsimple

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.karyaanakbangsa.tracksymptomsimple.databinding.ActivityPredictionResultBinding

class PredictionResultActivity : AppCompatActivity() {
    private lateinit var binding: ActivityPredictionResultBinding

    companion object {
        const val EXTRA_DISEASE = "extra_disease"
        const val EXTRA_DESCRIPTION = "extra_description"
        const val EXTRA_PROBABILITY = "extra_probability"
        const val EXTRA_PRECAUTION = "extra_precaution"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPredictionResultBinding.inflate(layoutInflater)
        setContentView(binding.root)

        supportActionBar?.title = "Prediction Result"

        val extraDisease = intent.getStringExtra(EXTRA_DISEASE)
        val extraDescription = intent.getStringExtra(EXTRA_DESCRIPTION)
        val extraProbability = intent.getStringExtra(EXTRA_PROBABILITY)
        val extraPrecaution = intent.getStringExtra(EXTRA_PRECAUTION)

        binding.tvDisease.text = extraDisease
        binding.tvDescription.text = "Description : $extraDescription"
        binding.tvProbability.text =
            "The chance you might get this disease is by $extraProbability %"
        binding.tvPrecaution.text = "Precaution : $extraPrecaution"
    }
}