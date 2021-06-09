package com.karyaanakbangsa.tracksymptom.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [Symptoms::class], version = 1, exportSchema = false)
abstract class SymptomsDatabase : RoomDatabase() {

    abstract fun symptomsDao(): SymptomsDao

    companion object {
        @Volatile
        private var INSTANCE: SymptomsDatabase? = null

        fun getDatabase(context: Context): SymptomsDatabase {
            val tempInstance = INSTANCE
            if (tempInstance != null) {
                return tempInstance
            }
            synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    SymptomsDatabase::class.java,
                    "symptoms_database.db"
                )
                    .createFromAsset("database/symptoms.db")
                    .build()
                INSTANCE = instance
                return instance
            }
        }
    }
}