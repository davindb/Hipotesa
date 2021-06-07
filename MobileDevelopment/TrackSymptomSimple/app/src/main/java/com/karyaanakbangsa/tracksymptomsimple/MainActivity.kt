package com.karyaanakbangsa.tracksymptomsimple

import android.content.Intent
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.EditText
import android.widget.Toast
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
            var symptom1 = binding.atv1.text.toString()
            symptom1.trim()
            var symptom2 = binding.atv2.text.toString()
            symptom2.trim()
            var symptom3 = binding.atv3.text.toString()
            symptom3.trim()
            var symptom4 = binding.atv4.text.toString()
            symptom4.trim()
            var symptom5 = binding.atv5.text.toString()
            symptom5.trim()

            if(symptom1.isEmpty()){
                symptom1 = "0"
            }
            if(symptom2.isEmpty()){
                symptom2 = "0"
            }
            if(symptom3.isEmpty()){
                symptom3 = "0"
            }
            if(symptom4.isEmpty()){
                symptom4 = "0"
            }
            if(symptom5.isEmpty()){
                symptom5 = "0"
            }

            val post = SymptomsBody(symptom1, symptom2, symptom3, symptom4, symptom5)

            if (countFilledFields() >= 3) {

                viewModel.pushPost(post)
                viewModel.getResponse().observe(this, {
                    if (it !== null) {
                        val disease = it.Disease
                        val description = it.Description
                        val probability = String.format("%.2f",it.Probability)
                        val precaution = it.Precaution.toString()
                        Intent(this@MainActivity, PredictionResultActivity::class.java).also{i->
                            i.putExtra(PredictionResultActivity.EXTRA_DISEASE, disease)
                            i.putExtra(PredictionResultActivity.EXTRA_DESCRIPTION, description)
                            i.putExtra(PredictionResultActivity.EXTRA_PROBABILITY, probability)
                            i.putExtra(PredictionResultActivity.EXTRA_PRECAUTION, precaution)
                            startActivity(i)
                        }
                    } else {
                        Toast.makeText(this, "Error", Toast.LENGTH_LONG).show()
                    }
                })
            } else {
                Toast.makeText(this, "Please insert 3 symptoms minimum", Toast.LENGTH_SHORT)
                    .show()
            }
        }

    }

    private fun countFilledFields(): Int {
        val editTexts: ArrayList<EditText> = ArrayList()
        editTexts.add(binding.atv1)
        editTexts.add(binding.atv2)
        editTexts.add(binding.atv3)
        editTexts.add(binding.atv4)
        editTexts.add(binding.atv5)
        var filledNumber = 0
        for (i in 0 until editTexts.size) {
            if (editTexts[i].text != null && !editTexts[i].text.toString()
                    .matches("".toRegex())
            ) {
                filledNumber += 1
            }
        }
        return filledNumber
    }
}