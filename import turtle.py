 package com.example.francesco.askzelda;

    import android.support.v7.app.AppCompatActivity;
    import android.os.Bundle;
    import android.view.View;
    import android.view.Window;
    import android.widget.Button;
    import android.widget.CheckBox;
    import android.widget.EditText;
    import android.widget.RadioButton;
    import android.widget.TextView;
    import android.widget.Toast;

    public class MainActivity extends AppCompatActivity {
        Button submit;
        int correctAnswers = 0;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
        }

        //Make sure that user can only choose the two of the answers not all of them.
        public void checkTwoBox(View view) {
            CheckBox firstcheck = (CheckBox) findViewById(R.id.optionQ3_1);
            CheckBox secondcheck = (CheckBox) findViewById(R.id.optionQ3_2);
            CheckBox thirdcheck = (CheckBox) findViewById(R.id.optionQ3_3);

            if (firstcheck.isChecked() && secondcheck.isChecked()) {
                thirdcheck.setChecked(false);
            }
            if (thirdcheck.isChecked() && secondcheck.isChecked()) {
                firstcheck.setChecked(false);
            }
            if (thirdcheck.isChecked() && firstcheck.isChecked()) {
                secondcheck.setChecked(false);
            }
        }

        //Show the result

        public void submitResult(View view) {
            //figure out if the user choose the right answer
            RadioButton firstRightBox = (RadioButton) findViewById(R.id.option1_rb);
            boolean hasClickedFirst1 = firstRightBox.isChecked();

            RadioButton secondRightBox = (RadioButton) findViewById(R.id.optionQ2_2_rb);
            boolean hasClickedSecond2 = secondRightBox.isChecked();

            CheckBox thirdRightBox = (CheckBox) findViewById(R.id.optionQ3_1);
            boolean hasClickedThird1 = thirdRightBox.isChecked();

            CheckBox thirdSecondRightBox = (CheckBox) findViewById(R.id.optionQ3_3);
            boolean hasClickedThird3 = thirdSecondRightBox.isChecked();

            EditText answerText = (EditText) findViewById(R.id.question_4_editText);
            String MasterSword = answerText.getText().toString();

            //figure out if the user choose the wrong answer

            RadioButton firstWrongBox = (RadioButton) findViewById(R.id.option2_rb);
            boolean hasClickedFirst2 = firstWrongBox.isChecked();

            RadioButton firstWrongBox2 = (RadioButton) findViewById(R.id.option3_rb);
            boolean hasClickedFirst3 = firstWrongBox2.isChecked();

            RadioButton secondWrongBox = (RadioButton) findViewById(R.id.optionQ2_1_rb);
            boolean hasClickedSecond1 = secondWrongBox.isChecked();

            RadioButton secondWrongBox2 = (RadioButton) findViewById(R.id.optionQ2_3_rb);
            boolean hasClickedSecond3 = secondWrongBox2.isChecked();

            CheckBox thirdWrongBox = (CheckBox) findViewById(R.id.optionQ3_2);
            boolean hasClickedThird2 = thirdWrongBox.isChecked();

            int correctAnswer = calculateCorrectAnswer(hasClickedFirst1, hasClickedSecond2, hasClickedThird1, hasClickedThird2, hasClickedThird3, MasterSword);
            int wrongAnswer = calculateWrongAnswer(hasClickedFirst2, hasClickedFirst3, hasClickedSecond1, hasClickedSecond3, hasClickedThird2, hasClickedThird1, hasClickedThird3, MasterSword);
            int emptyAnswer = calculateEmptyAnswer(hasClickedFirst1, hasClickedSecond2, hasClickedThird1, hasClickedThird2, hasClickedThird3, MasterSword, hasClickedFirst2, hasClickedFirst3, hasClickedSecond1, hasClickedSecond3);
            String quizMessage = createOrderSummary(correctAnswer, wrongAnswer, emptyAnswer);

            // Toast Message
            String toast_1 = getString(R.string.toast_1);
            String toast_2 = getString(R.string.toast_2);
            String toast_3 = getString(R.string.toast_3);

            Toast.makeText(MainActivity.this,toast_1 + " " + correctAnswer + " " + toast_2 + " \n" + toast_3, Toast.LENGTH_LONG).show();

            displayMessage(quizMessage);
        }

        private String createOrderSummary(int correctAnswer, int wrongAnswer, int emptyAnswer) {
            String msg1 = getString(R.string.thank1);
            String msg2 = getString(R.string.thank2);
            String msg3 = getString(R.string.total_correct);
            String msg4 = getString(R.string.total_wrong);
            String msg5 = getString(R.string.total_empty1);
            String msg6 = getString(R.string.total_empty2);
            String msg7 = getString(R.string.final_msg1);
            String msg8 = getString(R.string.final_msg2);
            String msg9 = getString(R.string.final_msg3);

            String quizMessage = msg1 + " " + " " + msg2;
            quizMessage += "\n" + msg3 + " " + correctAnswer;
            quizMessage += "\n" + msg4 + " " + wrongAnswer;
            quizMessage += "\n" + msg5 + " " + emptyAnswer + " " + msg6;
            if (correctAnswer <= wrongAnswer) {
                quizMessage += "\n" + msg7;
            } else {
                quizMessage += "\n" + msg8;
            }
            quizMessage += "\n" + msg9;
            return quizMessage;
        }

    //Calculates correct

        public int calculateCorrectAnswer(boolean first1, boolean second2, boolean third1, boolean third2, boolean third3, String LeoTolstoy) {
            int correct = 0;

            if (first1) {
                correct = correct + 1;
            }
            if (second2) {
                correct = correct + 1;
            }
            if (third1 & third3) {
                correct = correct + 1;
            }
            if (LeoTolstoy.equals("Master Sword")) {
                correct = correct + 1;
            }
            int correctAnswer = correct;
            return correctAnswer;
        }

    //Calculates false

        public int calculateWrongAnswer(boolean first2, boolean first3, boolean second1, boolean second3, boolean third2, boolean third1, boolean third3, String MasterSowrd) {
            int wrong = 0;

            if (first2) {
                wrong = wrong + 1;
            }
            if (first3) {
                wrong = wrong + 1;
            }
            if (second1) {
                wrong = wrong + 1;
            }
            if (second3) {
                wrong = wrong + 1;
            }
            if ((third1 & third2) || (third3 & third2) || (third3 & third2 & third1)) {
                wrong = wrong + 1;
            }
            if (!MasterSowrd.equals("Master Sword") && !MasterSowrd.equals("")) {
                wrong = wrong + 1;
            }
            int wrongAnswer = wrong;
            return wrongAnswer;
        }

        //calculate empty questions
        public int calculateEmptyAnswer(boolean first1, boolean second2, boolean third1, boolean third2, boolean third3, String MasterSowrd, boolean first2, boolean first3, boolean second1, boolean second3) {
            int empty = 0;

            if (!first1 && !first2 && !first3) {
                empty = empty + 1;
            }
            if (!second1 && !second2 && !second3) {
                empty = empty + 1;
            }
            if ((!third1 && !third3 && !third2) || (third1 && !third3 && !third2) || (third3 && !third1 && !third2) || (third2 && !third1 && !third3)) {
                empty = empty + 1;
            }
            if (MasterSowrd.equals("")) {
                empty = empty + 1;
            }
            int emptyAnswer = empty;
            return emptyAnswer;
        }

        //This method displays the given text on the screen.
        public void displayMessage(String message) {
            TextView orderSummaryTextView = (TextView) findViewById(R.id.result_text_view);
            orderSummaryTextView.setText(message);
        }
    }