package com.karyaanakbangsa.tracksymptom.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.karyaanakbangsa.tracksymptom.data.Symptoms
import com.karyaanakbangsa.tracksymptom.databinding.SymptomItemBinding

class RecyclerViewAdapter : RecyclerView.Adapter<RecyclerViewAdapter.SymptomsViewHolder>() {

    private var symptomsList = emptyList<Symptoms>()

    class SymptomsViewHolder(val binding: SymptomItemBinding) :
        RecyclerView.ViewHolder(binding.root) {
        fun bind(symptoms: Symptoms) {
            with(binding) {
                cbSymptom.text = symptoms.symptomsName
            }
        }

    }

    fun setData(symptoms: List<Symptoms>){
        this.symptomsList = symptoms
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): SymptomsViewHolder {
        val view = SymptomItemBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return SymptomsViewHolder(view)
    }

    override fun onBindViewHolder(holder: SymptomsViewHolder, position: Int) {
        holder.bind(symptomsList[position])
    }

    override fun getItemCount(): Int {
        return symptomsList.size
    }
}