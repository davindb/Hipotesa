package com.karyaanakbangsa.tracksymptomsimple

import android.os.Bundle
import android.widget.ArrayAdapter
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import com.karyaanakbangsa.tracksymptomsimple.data.SymptomsBody
import com.karyaanakbangsa.tracksymptomsimple.databinding.ActivityMainBinding
import com.karyaanakbangsa.tracksymptomsimple.repository.Repository

class MainActivity : AppCompatActivity() {

    private lateinit var viewModel: MainViewModel
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        supportActionBar?.title = getString(R.string.action_bar_title)

        val repository = Repository()
        val viewModelFactory = MainViewModelFactory(repository)
        viewModel = ViewModelProvider(this, viewModelFactory).get(MainViewModel::class.java)
        val symptoms = resources.getStringArray(R.array.symptoms)
        val arrayAdapter = ArrayAdapter(this, R.layout.dropdown_item, symptoms)
        binding.atv1.setAdapter(arrayAdapter)
        binding.atv2.setAdapter(arrayAdapter)
        binding.atv3.setAdapter(arrayAdapter)
        binding.atv4.setAdapter(arrayAdapter)
        binding.atv5.setAdapter(arrayAdapter)

        binding.btnPredict.setOnClickListener {
            val symptom1 = binding.atv1.text.toString()
            val symptom2 = binding.atv1.text.toString()
            val symptom3 = binding.atv1.text.toString()
            val symptom4 = binding.atv1.text.toString()
            val symptom5 = binding.atv1.text.toString()
            val post = SymptomsBody(symptom1, symptom2, symptom3, symptom4, symptom5)
            viewModel.pushPost(post)
            viewModel.getResponse().observe(this,{
                binding.tvDisease.text = it.Disease
                binding.tvDescription.text = it.Description
                binding.tvProbability.text = it.Probability.toString()
                binding.tvPrecaution.text = it.Precaution.toString()
            })
        }

    }

}