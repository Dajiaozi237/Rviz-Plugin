#ifndef CALCULATOR_PANEL_HPP_
#define CALCULATOR_PANEL_HPP_

#include <QWidget>
#include <QRadioButton>
#include "rviz_common/panel.hpp"

class QLineEdit;
class QLabel;
class QPushButton;

namespace calculator_plugin
{

class CalculatorPanel : public rviz_common::Panel
{
  Q_OBJECT

public:
  explicit CalculatorPanel(QWidget* parent = nullptr);

protected Q_SLOTS:
  void calculate();
  void updateOperation();

private:
  // UI elements
  QLineEdit* input_a_;
  QLineEdit* input_b_;
  QLineEdit* input_c_;
  QRadioButton* add_radio_;
  QRadioButton* mul_radio_;
  QPushButton* count_button_;
  QLabel* result_label_;
};

} // namespace calculator_plugin

#endif // CALCULATOR_PANEL_HPP_
