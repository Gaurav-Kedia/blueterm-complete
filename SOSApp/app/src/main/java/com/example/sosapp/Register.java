package com.example.sosapp;

import android.app.Activity;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.example.sosapp.data.Contract;
import com.example.sosapp.data.DbHelper;

public class Register extends AppCompatActivity {

    EditText n1, n2, n3, n4, n5 , num1, num2, num3, num4, num5, messaget;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.contact_activity);

        n1 = (EditText) findViewById(R.id.n1);
        n2 = (EditText) findViewById(R.id.n2);
        n3 = (EditText) findViewById(R.id.n3);
        n4 = (EditText) findViewById(R.id.n4);
        n5 = (EditText) findViewById(R.id.n5);

        num1 = (EditText) findViewById(R.id.num1);
        num2 = (EditText) findViewById(R.id.num2);
        num3 = (EditText) findViewById(R.id.num3);
        num4 = (EditText) findViewById(R.id.num4);
        num5 = (EditText) findViewById(R.id.num5);

        messaget = (EditText) findViewById(R.id.message_txt);

    }

    public void save_to_SqLite(View view) {
        String s1, s2, s3, s4, s5, sum1, sum2, sum3, sum4, sum5, msg;
        s1 = n1.getText().toString().trim();
        s2 = n2.getText().toString().trim();
        s3 = n3.getText().toString().trim();
        s4 = n4.getText().toString().trim();
        s5 = n5.getText().toString().trim();

        sum1 = num1.getText().toString().trim();
        sum2 = num2.getText().toString().trim();
        sum3 = num3.getText().toString().trim();
        sum4 = num4.getText().toString().trim();
        sum5 = num5.getText().toString().trim();

        msg = messaget.getText().toString().trim();
        DbHelper Db = new DbHelper(Register.this);
        SQLiteDatabase db = Db.getWritableDatabase();

        ContentValues cv1 = new ContentValues();
        cv1.put(Contract.Entry.NAME, s1);
        cv1.put(Contract.Entry.NUMBER, sum1);

        ContentValues cv2 = new ContentValues();
        cv2.put(Contract.Entry.NAME, s2);
        cv2.put(Contract.Entry.NUMBER, sum2);

        ContentValues cv3 = new ContentValues();
        cv3.put(Contract.Entry.NAME, s3);
        cv3.put(Contract.Entry.NUMBER, sum3);

        ContentValues cv4 = new ContentValues();
        cv4.put(Contract.Entry.NAME, s4);
        cv4.put(Contract.Entry.NUMBER, sum4);

        ContentValues cv5 = new ContentValues();
        cv5.put(Contract.Entry.NAME, s5);
        cv5.put(Contract.Entry.NUMBER, sum5);

        db.insert(Contract.Entry.TABLE_NAME, null, cv1);
        db.insert(Contract.Entry.TABLE_NAME, null, cv2);
        db.insert(Contract.Entry.TABLE_NAME, null, cv3);
        db.insert(Contract.Entry.TABLE_NAME, null, cv4);
        db.insert(Contract.Entry.TABLE_NAME, null, cv5);

        Toast.makeText(Register.this,"Saved",Toast.LENGTH_SHORT).show();

    }
}
