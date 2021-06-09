package com.karyaanakbangsa.tracksymptom.ui

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.LinearLayoutManager
import com.karyaanakbangsa.tracksymptom.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var mainViewModel: MainViewModel
    private lateinit var adapter: RecyclerViewAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //RecyclerView
        adapter = RecyclerViewAdapter()

        //ViewModel
        mainViewModel = ViewModelProvider(this).get(MainViewModel::class.java)
        mainViewModel.readAllData.observe(this, { symptoms ->
            adapter.setData(symptoms)
        })
        recyclerViewConfig()
    }

    private fun recyclerViewConfig() {
        binding.apply {
            rvSymptoms.layoutManager = LinearLayoutManager(binding.rvSymptoms.context)
            rvSymptoms.setHasFixedSize(true)
            rvSymptoms.adapter = adapter
            rvSymptoms.addItemDecoration(
                DividerItemDecoration(
                    binding.rvSymptoms.context,
                    DividerItemDecoration.VERTICAL
                )
            )
        }
    }
}
