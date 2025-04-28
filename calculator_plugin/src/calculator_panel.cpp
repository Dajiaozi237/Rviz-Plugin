#include "calculator_panel.hpp"

#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QRadioButton>
#include <QPushButton>
#include <QButtonGroup>

namespace calculator_plugin
{

CalculatorPanel::CalculatorPanel(QWidget* parent)
  : rviz_common::Panel(parent)
{
  // Create input fields
  QVBoxLayout* layout = new QVBoxLayout;
  
  input_a_ = new QLineEdit;
  input_b_ = new QLineEdit;
  input_c_ = new QLineEdit;

  layout->addWidget(new QLabel("Number A:"));
  layout->addWidget(input_a_);
  layout->addWidget(new QLabel("Number B:"));
  layout->addWidget(input_b_);
  layout->addWidget(new QLabel("Number C:"));
  layout->addWidget(input_c_);

  // Operation selection
  QHBoxLayout* op_layout = new QHBoxLayout;
  add_radio_ = new QRadioButton("Add");
  mul_radio_ = new QRadioButton("Multiply");
  add_radio_->setChecked(true);
  
  op_layout->addWidget(add_radio_);
  op_layout->addWidget(mul_radio_);
  layout->addLayout(op_layout);

  // Calculate button
  count_button_ = new QPushButton("Count");
  layout->addWidget(count_button_);

  // Result display
  result_label_ = new QLabel("Result will appear here");
  layout->addWidget(result_label_);

  setLayout(layout);

  // Connect signals
  connect(count_button_, &QPushButton::clicked, this, &CalculatorPanel::calculate);
  connect(add_radio_, &QRadioButton::toggled, this, &CalculatorPanel::updateOperation);
}

void CalculatorPanel::calculate()
{
  try {
    double a = input_a_->text().toDouble();
    double b = input_b_->text().toDouble();
    double c = input_c_->text().toDouble();
    
    double result = 0;
    if (add_radio_->isChecked()) {
      result = a + b + c;
      result_label_->setText(QString("Sum: %1").arg(result));
    } else {
      result = a * b * c;
      result_label_->setText(QString("Product: %1").arg(result));
    }
  } catch (...) {
    result_label_->setText("Invalid input!");
  }
}

void CalculatorPanel::updateOperation()
{
  // Optional: Add visual feedback when operation changes
  if (add_radio_->isChecked()) {
    count_button_->setText("Add");
  } else {
    count_button_->setText("Multiply");
  }
}

} // namespace calculator_plugin

#include "pluginlib/class_list_macros.hpp"
PLUGINLIB_EXPORT_CLASS(calculator_plugin::CalculatorPanel, rviz_common::Panel)
